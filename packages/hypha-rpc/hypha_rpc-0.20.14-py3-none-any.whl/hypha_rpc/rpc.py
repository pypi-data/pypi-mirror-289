"""Provide the RPC."""

import asyncio
import inspect
import json
import io
import logging
import math
import sys
import traceback
import weakref
from collections import OrderedDict
from functools import partial, reduce
from .utils import ObjectProxy, DefaultObjectProxy

import msgpack
import shortuuid

from .utils import (
    MessageEmitter,
    format_traceback,
    callable_doc,
    convert_case,
)
from .utils.schema import schema_function

CHUNK_SIZE = 1024 * 500
API_VERSION = "0.20.0"
ALLOWED_MAGIC_METHODS = ["__enter__", "__exit__"]
IO_PROPS = [
    "name",  # file name
    "size",  # size in bytes
    "path",  # file path
    "type",  # type type
    "fileno",
    "seek",
    "truncate",
    "detach",
    "write",
    "read",
    "read1",
    "readall",
    "close",
    "closed",
    "__enter__",
    "__exit__",
    "flush",
    "isatty",
    "__iter__",
    "__next__",
    "readable",
    "readline",
    "readlines",
    "seekable",
    "tell",
    "writable",
    "writelines",
]

logging.basicConfig(stream=sys.stdout)
logger = logging.getLogger("RPC")
logger.setLevel(logging.WARNING)


def index_object(obj, ids):
    """Index an object."""
    if isinstance(ids, str):
        return index_object(obj, ids.split("."))
    elif len(ids) == 0:
        return obj
    else:
        if isinstance(obj, dict):
            _obj = obj[ids[0]]
        elif isinstance(obj, (list, tuple)):
            _obj = obj[int(ids[0])]
        else:
            _obj = getattr(obj, ids[0])
        return index_object(_obj, ids[1:])


def _get_schema(obj, name=None, skip_context=False):
    """Get schema."""
    if isinstance(obj, dict):
        schema = {}
        for k, v in obj.items():
            schema[k] = _get_schema(v, k, skip_context=skip_context)
        return schema
    elif isinstance(obj, (list, tuple)):
        return [
            _get_schema(
                v,
                skip_context=skip_context,
            )
            for v in obj
        ]
    elif callable(obj):
        if hasattr(obj, "__schema__"):
            schema = obj.__schema__.copy()
            if name:
                schema["name"] = name
                obj.__schema__["name"] = name
            if skip_context:
                if "parameters" in schema:
                    if "properties" in schema["parameters"]:
                        schema["parameters"]["properties"].pop("context", None)
            return {"type": "function", "function": schema}
        else:
            return {"type": "function"}
    elif isinstance(obj, (int, float)):
        return {"type": "number"}
    elif isinstance(obj, str):
        return {"type": "string"}
    elif isinstance(obj, bool):
        return {"type": "boolean"}
    elif obj is None:
        return {"type": "null"}
    else:
        return {}


def _annotate_service(service, service_type_info):
    service_type_info = ObjectProxy.toDict(service_type_info)

    def validate_keys(service_dict, schema_dict, path="root"):
        # Validate that all keys in schema_dict exist in service_dict
        for key in schema_dict:
            if key not in service_dict:
                raise KeyError(f"Missing key '{key}' in service at path '{path}'")

        # Check for any unexpected keys in service_dict
        for key in service_dict:
            if key != "type" and key not in schema_dict:
                raise KeyError(f"Unexpected key '{key}' in service at path '{path}'")

    def annotate_recursive(new_service, schema_info, path="root"):
        if isinstance(new_service, dict):
            validate_keys(new_service, schema_info, path)
            for k, v in new_service.items():
                new_path = f"{path}.{k}"
                if isinstance(v, dict):
                    annotate_recursive(v, schema_info[k], new_path)
                elif callable(v):
                    if k in schema_info:
                        assert schema_info[k]["type"] == "function"
                        if schema_info[k].get("function"):
                            annotation = schema_info[k]["function"]
                        else:
                            annotation = {"name": k, "parameters": {}}

                        new_service[k] = schema_function(
                            v,
                            name=annotation["name"],
                            description=annotation.get("description", ""),
                            parameters=annotation["parameters"],
                        )
                    else:
                        raise KeyError(
                            f"Missing schema for function '{k}' at path '{new_path}'"
                        )
        elif isinstance(new_service, (list, tuple)):
            if len(new_service) != len(schema_info):
                raise ValueError(f"Length mismatch at path '{path}'")
            for k, v in enumerate(new_service):
                new_path = f"{path}[{k}]"
                if isinstance(v, (dict, list, tuple)):
                    annotate_recursive(v, schema_info[k], new_path)
                elif callable(v):
                    if k in schema_info:
                        assert schema_info[k]["type"] == "function"
                        if schema_info[k].get("function"):
                            annotation = schema_info[k]["function"]
                        else:
                            annotation = {"name": k, "parameters": {}}

                        new_service[k] = schema_function(
                            v,
                            name=annotation["name"],
                            description=annotation.get("description", ""),
                            parameters=annotation["parameters"],
                        )
                    else:
                        raise KeyError(
                            f"Missing schema for function at index {k} in path '{new_path}'"
                        )

    validate_keys(service, service_type_info["definition"])
    annotate_recursive(service, service_type_info["definition"])
    return service


class RemoteException(Exception):
    """Represent a remote exception."""

    pass


class Timer:
    """Represent a timer."""

    def __init__(self, timeout, callback, *args, label="timer", **kwargs):
        """Set up instance."""
        self._timeout = timeout
        self._callback = callback
        self._task = None
        self._args = args
        self._kwrags = kwargs
        self._label = label
        self.started = False

    def start(self):
        """Start the timer."""
        if not self.started:
            self._task = asyncio.ensure_future(self._job())
            self.started = True
        else:
            self.reset()

    async def _job(self):
        """Handle a job."""
        await asyncio.sleep(self._timeout)
        ret = self._callback(*self._args, **self._kwrags)
        if ret is not None and inspect.isawaitable(ret):
            await ret

    def clear(self):
        """Clear the timer."""
        if self._task:
            self._task.cancel()
            self._task = None
            self.started = False
        else:
            logger.warning("Clearing a timer (%s) which is not started", self._label)

    def reset(self):
        """Reset the timer."""
        if self._task is None:
            self.start()
        else:
            self._task.cancel()
            self._task = asyncio.ensure_future(self._job())


class RPC(MessageEmitter):
    """Represent the RPC."""

    def __init__(
        self,
        connection,
        client_id=None,
        default_context=None,
        name=None,
        codecs=None,
        method_timeout=None,
        max_message_buffer_size=0,
        loop=None,
        workspace=None,
        silent=False,
        app_id=None,
    ):
        """Set up instance."""
        self._codecs = codecs or {}
        assert client_id and isinstance(client_id, str)
        assert client_id is not None, "client_id is required"
        self._client_id = client_id
        self._name = name
        self._app_id = app_id or "*"
        self._local_workspace = workspace
        self._silent = silent
        self.default_context = default_context or {}
        self._method_annotations = weakref.WeakKeyDictionary()
        self._max_message_buffer_size = max_message_buffer_size
        self._chunk_store = {}
        self._method_timeout = 30 if method_timeout is None else method_timeout
        self._remote_logger = logger
        self.loop = loop or asyncio.get_event_loop()
        super().__init__(self._remote_logger)

        self._services = {}
        self._object_store = {
            "services": self._services,
        }

        if connection:
            self.add_service(
                {
                    "id": "built-in",
                    "type": "built-in",
                    "name": f"Builtin services for {self._local_workspace}/{self._client_id}",
                    "config": {"require_context": True, "visibility": "public"},
                    "ping": self._ping,
                    "get_service": self.get_local_service,
                    "message_cache": {
                        "create": self._create_message,
                        "append": self._append_message,
                        "process": self._process_message,
                        "remove": self._remove_message,
                    },
                }
            )
            self.on("method", self._handle_method)
            self.on("error", self._error)

            assert hasattr(connection, "emit_message") and hasattr(
                connection, "on_message"
            )
            assert hasattr(connection, "manager_id"), "Connection must have manager_id"
            self._emit_message = connection.emit_message
            connection.on_message(self._on_message)
            self._connection = connection

            async def on_connected(connection_info):
                if not self._silent and self._connection.manager_id:
                    logger.info("Connection established, reporting services...")
                    manager = await self.get_manager_service(10, "snake")
                    for service in list(self._services.values()):
                        service_info = self._extract_service_info(service)
                        await manager.register_service(service_info)
                else:
                    logger.info("Connection established: %s", connection_info)
                self._fire("connected", connection_info)

            connection.on_connected(on_connected)
            self.loop.create_task(on_connected(None))
        else:

            async def _emit_message(_):
                logger.info("No connection to emit message")

            self._emit_message = _emit_message

        self.check_modules()

    def register_codec(self, config: dict):
        """Register codec."""
        assert "name" in config
        assert "encoder" in config or "decoder" in config
        if "type" in config:
            for tp in list(self._codecs.keys()):
                codec = self._codecs[tp]
                if codec.type == config["type"] or tp == config["name"]:
                    logger.info("Removing duplicated codec: " + tp)
                    del self._codecs[tp]

        self._codecs[config["name"]] = DefaultObjectProxy.fromDict(config)

    async def _ping(self, msg: str, context=None):
        """Handle ping."""
        assert msg == "ping"
        return "pong"

    async def ping(self, client_id: str, timeout=1):
        """Send a ping."""
        method = self._generate_remote_method(
            {
                "_rtarget": client_id,
                "_rmethod": "services.built-in.ping",
                "_rpromise": True,
                "_rdoc": "Ping the remote client",
            }
        )
        assert (await asyncio.wait_for(method("ping"), timeout)) == "pong"

    def _create_message(
        self, key: str, heartbeat: bool = False, overwrite: bool = False, context=None
    ):
        """Create a message."""
        if heartbeat:
            if key not in self._object_store:
                raise Exception(f"session does not exist anymore: {key}")
            self._object_store[key]["timer"].reset()

        if "message_cache" not in self._object_store:
            self._object_store["message_cache"] = {}
        if not overwrite and key in self._object_store["message_cache"]:
            raise Exception(
                "Message with the same key (%s) already exists in the cache store, "
                "please use overwrite=True or remove it first.",
                key,
            )

        self._object_store["message_cache"][key] = b""

    def _append_message(
        self, key: str, data: bytes, heartbeat: bool = False, context=None
    ):
        """Append a message."""
        if heartbeat:
            if key not in self._object_store:
                raise Exception(f"session does not exist anymore: {key}")
            self._object_store[key]["timer"].reset()
        cache = self._object_store["message_cache"]
        if key not in cache:
            raise KeyError(f"Message with key {key} does not exists.")
        assert isinstance(data, bytes)
        cache[key] += data

    def _remove_message(self, key: str, context=None):
        """Remove a message."""
        cache = self._object_store["message_cache"]
        if key not in cache:
            raise KeyError(f"Message with key {key} does not exists.")
        del cache[key]

    def _process_message(self, key: str, heartbeat: bool = False, context=None):
        """Process a message."""
        if heartbeat:
            if key not in self._object_store:
                raise Exception(f"session does not exist anymore: {key}")
            self._object_store[key]["timer"].reset()
        cache = self._object_store["message_cache"]
        assert context is not None, "Context is required"
        if key not in cache:
            raise KeyError(f"Message with key {key} does not exists.")
        logger.debug("Processing message %s (size=%d)", key, len(cache[key]))
        unpacker = msgpack.Unpacker(
            io.BytesIO(cache[key]), max_buffer_size=self._max_message_buffer_size
        )
        main = unpacker.unpack()
        # Make sure the fields are from trusted source
        main.update(
            {
                "from": context["from"],
                "to": context["to"],
                "user": context["user"],
            }
        )
        main["ctx"] = main.copy()
        main["ctx"].update(self.default_context)
        try:
            extra = unpacker.unpack()
            main.update(extra)
        except msgpack.exceptions.OutOfData:
            pass
        self._fire(main["type"], main)
        del cache[key]

    def _on_message(self, message):
        """Handle message."""
        if isinstance(message, str):
            main = json.loads(message)
            self._fire(main["type"], main)
        elif isinstance(message, bytes):
            unpacker = msgpack.Unpacker(
                io.BytesIO(message), max_buffer_size=CHUNK_SIZE * 2
            )
            main = unpacker.unpack()
            # Add trusted context to the method call
            main["ctx"] = main.copy()
            main["ctx"].update(self.default_context)
            try:
                extra = unpacker.unpack()
                main.update(extra)
            except msgpack.exceptions.OutOfData:
                pass
            self._fire(main["type"], main)
        elif isinstance(message, dict):
            self._fire(message["type"], message)
        else:
            raise Exception(f"Invalid message type: {type(message)}")

    def reset(self):
        """Reset."""
        self._event_handlers = {}
        self._services = {}

    async def disconnect(self):
        """Disconnect."""
        self._fire("disconnected")
        await self._connection.disconnect()

    async def get_manager_service(self, timeout=None, case_conversion=None):
        """Get remote root service."""
        assert self._connection.manager_id, "Manager id is not set"
        svc = await self.get_remote_service(
            f"*/{self._connection.manager_id}:default",
            timeout=timeout,
            case_conversion=case_conversion,
        )
        return svc

    def get_all_local_services(self):
        """Get all the local services."""
        return self._services

    def get_local_service(self, service_id: str, context=None):
        """Get a local service."""
        assert service_id is not None and context is not None
        ws, client_id = context["to"].split("/")
        assert client_id == self._client_id, "Services can only be accessed locally"

        service = self._services.get(service_id)
        if not service:
            raise KeyError("Service not found: %s", service_id)
        service["config"]["workspace"] = context["ws"]
        # allow access for the same workspace
        if service["config"].get("visibility", "protected") == "public":
            return service

        # allow access for the same workspace
        if context["ws"] == ws:
            return service

        raise Exception(
            f"Permission denied for getting protected service: {service_id}, workspace mismatch: {ws} != {context['ws']}"
        )

    async def get_remote_service(
        self, service_uri=None, timeout=None, case_conversion=None
    ):
        """Get a remote service."""
        timeout = timeout or self._method_timeout
        if service_uri is None and self._connection.manager_id:
            service_uri = "*/" + self._connection.manager_id
        elif ":" not in service_uri:
            service_uri = self._client_id + ":" + service_uri
        provider, service_id = service_uri.split(":")
        if "@" in service_id:
            service_id, app_id = service_id.split("@")
            if self._app_id and self._app_id != "*":
                assert app_id == str(
                    self._app_id
                ), f"App id mismatch: {app_id} != {self._app_id}"
        assert provider
        try:
            method = self._generate_remote_method(
                {
                    "_rtarget": provider,
                    "_rmethod": "services.built-in.get_service",
                    "_rpromise": True,
                    "_rdoc": "Get a remote service",
                }
            )
            svc = await asyncio.wait_for(method(service_id), timeout=timeout)
            svc["id"] = service_uri
            if case_conversion:
                return ObjectProxy.fromDict(convert_case(svc, case_conversion))
            else:
                return ObjectProxy.fromDict(svc)
        except Exception as exp:
            logger.warning("Failed to get remote service: %s: %s", service_id, exp)
            raise exp

    def _annotate_service_methods(
        self,
        a_object,
        object_id,
        require_context=False,
        run_in_executor=False,
        visibility="protected",
    ):
        if callable(a_object):
            # mark the method as a remote method that requires context
            method_name = ".".join(object_id.split(".")[1:])
            self._method_annotations[a_object] = {
                "require_context": (
                    (method_name in require_context)
                    if isinstance(require_context, (list, tuple))
                    else bool(require_context)
                ),
                "run_in_executor": run_in_executor,
                "method_id": "services." + object_id,
                "visibility": visibility,
            }
        elif isinstance(a_object, (dict, list, tuple)):
            items = (
                a_object.items() if isinstance(a_object, dict) else enumerate(a_object)
            )
            for key, val in items:
                if callable(val) and hasattr(val, "__rpc_object__"):
                    client_id = val.__rpc_object__["_rtarget"]
                    if "/" in client_id:
                        client_id = client_id.split("/")[1]
                    if self._client_id == client_id:
                        # Make sure we can modify the object
                        if isinstance(a_object, tuple):
                            a_object = list(a_object)
                        # recover local method
                        a_object[key] = index_object(
                            self._object_store, val.__rpc_object__["_rmethod"]
                        )
                        val = a_object[key]  # make sure it's annotated later
                    else:
                        raise Exception(
                            "Local method not found: "
                            f"{val.__rpc_object__['_rmethod']}, "
                            f"client id mismatch {self._client_id} != {client_id}"
                        )
                self._annotate_service_methods(
                    val,
                    object_id + "." + str(key),
                    require_context=require_context,
                    run_in_executor=run_in_executor,
                    visibility=visibility,
                )

    def add_service(self, api, overwrite=False):
        """Add a service (silently without triggering notifications)."""
        # convert and store it in a docdict
        # such that the methods are hashable
        if isinstance(api, dict):
            api = ObjectProxy.fromDict(
                {
                    a: api[a]
                    for a in api.keys()
                    if not a.startswith("_") or a in ALLOWED_MAGIC_METHODS
                }
            )
        elif inspect.isclass(type(api)):
            api = ObjectProxy.fromDict(
                {
                    a: getattr(api, a)
                    for a in dir(api)
                    if not a.startswith("_") or a in ALLOWED_MAGIC_METHODS
                }
            )
            # For class instance, we need set a default id
            api["id"] = api.get("id", "default")
        else:
            raise Exception("Invalid service object type: {}".format(type(api)))

        assert "id" in api and isinstance(
            api["id"], str
        ), f"Service id not found: {api}"

        if "name" not in api:
            api["name"] = api["id"]

        if "config" not in api:
            api["config"] = {}

        if "type" not in api:
            api["type"] = "generic"

        # require_context only applies to the top-level functions
        require_context, run_in_executor = False, False
        if bool(api["config"].get("require_context")):
            require_context = api["config"]["require_context"]
        if bool(api["config"].get("run_in_executor")):
            run_in_executor = True
        visibility = api["config"].get("visibility", "protected")
        assert visibility in ["protected", "public"]
        self._annotate_service_methods(
            api,
            api["id"],
            require_context=require_context,
            run_in_executor=run_in_executor,
            visibility=visibility,
        )
        if not overwrite and api["id"] in self._services:
            raise Exception(
                f"Service already exists: {api['id']}, please specify"
                f" a different id (not {api['id']}) or overwrite=True"
            )
        self._services[api["id"]] = api
        return api

    def _extract_service_info(self, service):
        service = ObjectProxy.toDict(service)
        config = service.get("config", {})
        config["workspace"] = config.get(
            "workspace", self._local_workspace or self._connection.workspace
        )
        skip_context = config.get("require_context", False)
        service_schema = _get_schema(service, skip_context=skip_context)
        service_info = {
            "config": ObjectProxy.fromDict(config),
            "id": f"{config['workspace']}/{self._client_id}:{service['id']}",
            "name": service.get("name", service["id"]),
            "description": service.get("description", None),
            "type": service.get("type", "generic"),
            "docs": service.get("docs", None),
            "app_id": self._app_id,
            "service_schema": service_schema,
        }
        return ObjectProxy.fromDict(service_info)

    async def get_service_schema(self, service):
        """Get service schema."""
        skip_context = service.get("config", {}).get("require_context", False)
        service_schema = _get_schema(service, skip_context=skip_context)
        return service_schema

    async def register_service(
        self,
        api: dict,
        overwrite: bool = False,
        notify: bool = True,
        check_type: bool = False,
    ):
        """Register a service."""
        if isinstance(api, ObjectProxy):
            api = ObjectProxy.toDict(api)
        manager = None
        if check_type and api.get("type"):
            try:
                manager = await self.get_manager_service(10, "snake")
                type_info = await manager.get_service_type(api["type"])
                api = _annotate_service(api, type_info)
            except Exception as exp:
                raise Exception(
                    f"Failed to get service type {api['type']}, error: {exp}"
                )

        service = self.add_service(api, overwrite=overwrite)
        service_info = self._extract_service_info(service)
        if notify:
            try:
                manager = manager or await self.get_manager_service(10, "snake")
                await manager.register_service(service_info)
            except Exception as exp:
                raise Exception(f"Failed to notify workspace manager: {exp}")
        return service_info

    async def unregister_service(self, service: dict, notify: bool = True):
        """Register a service."""
        if isinstance(service, str):
            service = self._services.get(service)
        if service["id"] not in self._services:
            raise Exception(f"Service not found: {service.get('id')}")
        del self._services[service["id"]]
        if notify:
            manager = await self.get_manager_service(10, "snake")
            await manager.unregister_service(service.id)

    def check_modules(self):
        """Check if all the modules exists."""
        try:
            import numpy as np

            self.NUMPY_MODULE = np
        except ImportError:
            self.NUMPY_MODULE = False
            logger.warning(
                "Failed to import numpy, ndarray encoding/decoding will not work"
            )

    def _encode_callback(
        self,
        name,
        callback,
        session_id,
        clear_after_called=False,
        timer=None,
        local_workspace=None,
    ):
        method_id = f"{session_id}.{name}"
        encoded = {
            "_rtype": "method",
            "_rtarget": (
                f"{local_workspace}/{self._client_id}"
                if local_workspace
                else self._client_id
            ),
            "_rmethod": method_id,
            "_rpromise": False,
        }

        def wrapped_callback(*args, **kwargs):
            try:
                callback(*args, **kwargs)
            except asyncio.InvalidStateError:
                # This probably means the task was cancelled
                logger.debug("Invalid state error in callback: %s", method_id)
            finally:
                if clear_after_called and session_id in self._object_store:
                    logger.info(
                        "Deleting session %s from %s", session_id, self._client_id
                    )
                    del self._object_store[session_id]
                if timer and timer.started:
                    timer.clear()

        return encoded, wrapped_callback

    def _encode_promise(
        self,
        resolve,
        reject,
        session_id,
        clear_after_called=False,
        timer=None,
        local_workspace=None,
    ):
        """Encode a group of callbacks without promise."""
        store = self._get_session_store(session_id, create=True)
        assert (
            store is not None
        ), f"Failed to create session store {session_id} due to invalid parent"
        encoded = {}

        if timer and reject and self._method_timeout:
            encoded["heartbeat"] = self._encode(
                timer.reset,
                session_id,
                local_workspace=local_workspace,
            )
            encoded["interval"] = self._method_timeout / 2
            store["timer"] = timer
        else:
            timer = None

        encoded["resolve"], store["resolve"] = self._encode_callback(
            "resolve",
            resolve,
            session_id,
            clear_after_called=clear_after_called,
            timer=timer,
            local_workspace=local_workspace,
        )
        encoded["reject"], store["reject"] = self._encode_callback(
            "reject",
            reject,
            session_id,
            clear_after_called=clear_after_called,
            timer=timer,
            local_workspace=local_workspace,
        )
        return encoded

    async def _send_chunks(self, package, target_id, session_id):
        remote_services = await self.get_remote_service(f"{target_id}:built-in")
        assert (
            remote_services.message_cache
        ), "Remote client does not support message caching for long message."
        message_cache = remote_services.message_cache
        message_id = session_id or shortuuid.uuid()
        await message_cache.create(message_id, bool(session_id))
        total_size = len(package)
        chunk_num = int(math.ceil(float(total_size) / CHUNK_SIZE))
        for idx in range(chunk_num):
            start_byte = idx * CHUNK_SIZE
            await message_cache.append(
                message_id,
                package[start_byte : start_byte + CHUNK_SIZE],
                bool(session_id),
            )
            logger.info(
                "Sending chunk %d/%d (%d bytes)",
                idx + 1,
                chunk_num,
                total_size,
            )
        logger.info("All chunks sent (%d)", chunk_num)
        await message_cache.process(message_id, bool(session_id))

    def emit(self, main_message, extra_data=None):
        """Emit a message."""
        assert (
            isinstance(main_message, dict) and "type" in main_message
        ), "Invalid message, must be an object with a `type` fields"
        if "to" not in main_message:
            self._fire(main_message["type"], main_message)
            return
        message_package = msgpack.packb(main_message)
        if extra_data:
            message_package = message_package + msgpack.packb(extra_data)
        total_size = len(message_package)
        if total_size <= CHUNK_SIZE + 1024:
            return self.loop.create_task(self._emit_message(message_package))
        else:
            raise Exception("Message is too large to send in one go.")

    def _generate_remote_method(
        self,
        encoded_method,
        remote_parent=None,
        local_parent=None,
        remote_workspace=None,
        local_workspace=None,
    ):
        """Return remote method."""
        target_id = encoded_method["_rtarget"]
        if remote_workspace and "/" not in target_id:
            if remote_workspace != target_id:
                target_id = remote_workspace + "/" + target_id
            # Fix the target id to be an absolute id
            encoded_method["_rtarget"] = target_id
        method_id = encoded_method["_rmethod"]
        with_promise = encoded_method.get("_rpromise", False)

        def remote_method(*arguments, **kwargs):
            """Run remote method."""
            arguments = list(arguments)
            # encode keywords to a dictionary and pass to the last argument
            if kwargs:
                arguments = arguments + [kwargs]

            fut = asyncio.Future()

            def resolve(result):
                if fut.done():
                    return
                fut.set_result(result)

            def reject(error):
                if fut.done():
                    return
                fut.set_exception(error)

            local_session_id = shortuuid.uuid()
            if local_parent:
                # Store the children session under the parent
                local_session_id = local_parent + "." + local_session_id
            store = self._get_session_store(local_session_id, create=True)
            if store is None:
                reject(RuntimeError(f"Failed to get session store {local_session_id}"))
                return
            store["target_id"] = target_id
            args = self._encode(
                arguments,
                session_id=local_session_id,
                local_workspace=local_workspace,
            )
            if self._local_workspace is None:
                from_client = self._client_id
            else:
                from_client = self._local_workspace + "/" + self._client_id

            main_message = {
                "type": "method",
                "from": from_client,
                "to": target_id,
                "method": method_id,
            }
            extra_data = {}
            if args:
                extra_data["args"] = args
            if kwargs:
                extra_data["with_kwargs"] = bool(kwargs)

            logger.info(
                "Calling remote method %s:%s, session: %s",
                target_id,
                method_id,
                local_session_id,
            )
            if remote_parent:
                # Set the parent session
                # Note: It's a session id for the remote, not the current client
                main_message["parent"] = remote_parent

            timer = None
            if with_promise:
                # Only pass the current session id to the remote
                # if we want to received the result
                # I.e. the session id won't be passed for promises themselves
                main_message["session"] = local_session_id
                method_name = f"{target_id}:{method_id}"
                timer = Timer(
                    self._method_timeout,
                    reject,
                    f"Method call time out: {method_name}",
                    label=method_name,
                )
                # By default, hypha will clear the session after the method is called
                # However, if the args contains _rintf === true, we will not clear the session
                clear_after_called = True
                for arg in args:
                    if (isinstance(arg, dict) and arg.get("_rintf")) or (
                        hasattr(arg, "_rintf") and arg._rintf == True
                    ):
                        clear_after_called = False
                        break

                extra_data["promise"] = self._encode_promise(
                    resolve=resolve,
                    reject=reject,
                    session_id=local_session_id,
                    clear_after_called=clear_after_called,
                    timer=timer,
                    local_workspace=local_workspace,
                )
            # The message consists of two segments, the main message and extra data
            message_package = msgpack.packb(main_message)
            if extra_data:
                message_package = message_package + msgpack.packb(extra_data)
            total_size = len(message_package)
            if total_size <= CHUNK_SIZE + 1024:
                emit_task = asyncio.ensure_future(self._emit_message(message_package))
            else:
                # send chunk by chunk
                emit_task = asyncio.ensure_future(
                    self._send_chunks(message_package, target_id, remote_parent)
                )

            def handle_result(fut):
                if fut.exception():
                    reject(
                        Exception(
                            "Failed to send the request when calling method "
                            f"({target_id}:{method_id}), error: {fut.exception()}"
                        )
                    )
                elif timer:
                    logger.info("Start watchdog timer.")
                    # Only start the timer after we send the message successfully
                    timer.start()

            emit_task.add_done_callback(handle_result)
            return fut

        # Generate debugging information for the method
        remote_method.__rpc_object__ = (
            encoded_method.copy()
        )  # pylint: disable=protected-access
        remote_method.__name__ = method_id.split(".")[-1]
        remote_method.__doc__ = encoded_method.get(
            "_rdoc", f"Remote method: {method_id}"
        )
        remote_method.__schema__ = encoded_method.get("_rschema")
        return remote_method

    def _log(self, info):
        logger.info("RPC Info: %s", info)

    def _error(self, error):
        logger.error("RPC Error: %s", error)

    def _call_method(
        self,
        method,
        args,
        kwargs,
        resolve=None,
        reject=None,
        heartbeat_task=None,
        method_name=None,
        run_in_executor=False,
    ):
        if not inspect.iscoroutinefunction(method) and run_in_executor:
            result = self.loop.run_in_executor(None, partial(method, *args, **kwargs))
        else:
            result = method(*args, **kwargs)
        if result is not None and inspect.isawaitable(result):

            async def _wait(result):
                try:
                    result = await result
                    if heartbeat_task:
                        heartbeat_task.cancel()
                    if resolve is not None:
                        return resolve(result)
                    elif result is not None:
                        logger.debug("returned value (%s): %s", method_name, result)
                except Exception as err:
                    traceback_error = traceback.format_exc()
                    logger.exception("Error in method (%s): %s", method_name, err)
                    if reject is not None:
                        return reject(Exception(format_traceback(traceback_error)))

            return asyncio.ensure_future(_wait(result))
        else:
            if heartbeat_task:
                heartbeat_task.cancel()
            if resolve is not None:
                return resolve(result)

    def get_client_info(self):
        """Get client info."""
        return {
            "id": self._client_id,
            "services": [
                self._extract_service_info(service)
                for service in self._services.values()
            ],
        }

    def _handle_method(self, data):
        """Handle RPC method call."""
        reject = None
        method_task = None
        heartbeat_task = None
        try:
            assert "method" in data and "ctx" in data and "from" in data
            method_name = f'{data["from"]}:{data["method"]}'
            remote_workspace = data["from"].split("/")[0]
            remote_client_id = data["from"].split("/")[1]
            # Make sure the target id is an absolute id
            data["to"] = (
                data["to"] if "/" in data["to"] else remote_workspace + "/" + data["to"]
            )
            data["ctx"]["to"] = data["to"]
            if self._local_workspace is None:
                local_workspace = data.get("to").split("/")[0]
            else:
                if self._local_workspace and self._local_workspace != "*":
                    assert data.get("to").split("/")[0] == self._local_workspace, (
                        "Workspace mismatch: "
                        f"{data.get('to').split('/')[0]} != {self._local_workspace}"
                    )
                local_workspace = self._local_workspace

            local_parent = data.get("parent")

            if "promise" in data:
                # Decode the promise with the remote session id
                # such that the session id will be passed to the remote
                # as a parent session id.
                promise = self._decode(
                    data["promise"],
                    remote_parent=data.get("session"),
                    local_parent=local_parent,
                    remote_workspace=remote_workspace,
                    local_workspace=local_workspace,
                )
                resolve, reject = promise["resolve"], promise["reject"]
                if "heartbeat" in promise and "interval" in promise:

                    async def heartbeat(interval):
                        while True:
                            try:
                                logger.debug(
                                    "Reset heartbeat timer: %s", data["method"]
                                )
                                await promise["heartbeat"]()
                            except asyncio.CancelledError:
                                if method_task and not method_task.done():
                                    method_task.cancel()
                                break
                            except Exception as exp:  # pylint: disable=broad-except
                                logger.error(
                                    "Failed to reset the heartbeat"
                                    " timer: %s, error: %s",
                                    data["method"],
                                    exp,
                                )
                                if method_task and not method_task.done():
                                    method_task.cancel()
                                break
                            if method_task and method_task.done():
                                logger.warning(
                                    "quiting heartbeat because the method task is done"
                                )
                                break
                            await asyncio.sleep(interval)

                    heartbeat_task = asyncio.ensure_future(
                        heartbeat(promise["interval"])
                    )
            else:
                resolve, reject = None, None

            try:
                method = index_object(self._object_store, data["method"])
            except Exception:
                logger.debug(
                    "Failed to find method %s at %s", method_name, self._client_id
                )
                raise Exception(f"Method not found: {method_name} at {self._client_id}")
            assert callable(method), f"Invalid method: {method_name}"

            # Check permission
            if method in self._method_annotations:
                # For services, it should not be protected
                if (
                    self._method_annotations[method].get("visibility", "protected")
                    == "protected"
                ):
                    if local_workspace != remote_workspace and (
                        remote_workspace != "*"
                        or remote_client_id != self._connection.manager_id
                    ):
                        raise PermissionError(
                            f"Permission denied for invoking protected method {method_name}, "
                            "workspace mismatch: "
                            f"{local_workspace} != {remote_workspace}"
                        )
            else:
                # For sessions, the target_id should match exactly
                session_target_id = self._object_store[data["method"].split(".")[0]][
                    "target_id"
                ]
                if (
                    local_workspace == remote_workspace
                    and session_target_id
                    and "/" not in session_target_id
                ):
                    session_target_id = local_workspace + "/" + session_target_id
                if session_target_id != data["from"]:
                    raise PermissionError(
                        f"Access denied for method call ({method_name}) "
                        f"from {data['from']}"
                        f" to target {session_target_id}"
                    )

            # Make sure the parent session is still open
            if local_parent:
                # The parent session should be a session
                # that generate the current method call.
                assert (
                    self._get_session_store(local_parent, create=False) is not None
                ), f"Parent session was closed: {local_parent}"
            if data.get("args"):
                args = self._decode(
                    data["args"],
                    remote_parent=data.get("session"),
                    remote_workspace=remote_workspace,
                )
            else:
                args = []
            if data.get("with_kwargs"):
                kwargs = args.pop()
            else:
                kwargs = {}

            if method in self._method_annotations and self._method_annotations[
                method
            ].get("require_context"):
                kwargs["context"] = data["ctx"]
            run_in_executor = (
                method in self._method_annotations
                and self._method_annotations[method].get("run_in_executor")
            )
            logger.info("Executing method: %s", method_name)
            method_task = self._call_method(
                method,
                args,
                kwargs,
                resolve,
                reject,
                heartbeat_task=heartbeat_task,
                method_name=method_name,
                run_in_executor=run_in_executor,
            )

        except Exception as err:
            # make sure we clear the heartbeat timer
            if (
                heartbeat_task
                and not heartbeat_task.cancelled()
                and not heartbeat_task.done()
            ):
                heartbeat_task.cancel()
            if callable(reject):
                reject(err)
                logger.debug("Error during calling method: %s", err)
            else:
                logger.exception("Error during calling method: %s", err)

    def encode(self, a_object, session_id=None):
        """Encode object."""
        return self._encode(
            a_object,
            session_id=session_id,
        )

    def _get_session_store(self, session_id, create=False):
        store = self._object_store
        levels = session_id.split(".")
        if create:
            for level in levels[:-1]:
                if level not in store:
                    return None
                store = store[level]

            # Create the last level
            if levels[-1] not in store:
                store[levels[-1]] = {}

            return store[levels[-1]]
        else:
            for level in levels:
                if level not in store:
                    return None
                store = store[level]
            return store

    def _encode(
        self,
        a_object,
        session_id=None,
        local_workspace=None,
    ):
        """Encode object."""
        if isinstance(a_object, (int, float, bool, str, bytes)) or a_object is None:
            return a_object

        if isinstance(a_object, tuple):
            a_object = list(a_object)

        if isinstance(a_object, dict):
            a_object = dict(a_object)

        # Reuse the remote object
        if hasattr(a_object, "__rpc_object__"):
            return a_object.__rpc_object__

        # skip if already encoded
        if isinstance(a_object, dict) and "_rtype" in a_object:
            # make sure the interface functions are encoded
            temp = a_object["_rtype"]
            del a_object["_rtype"]
            b_object = self._encode(
                a_object,
                session_id=session_id,
                local_workspace=local_workspace,
            )
            b_object["_rtype"] = temp
            return b_object

        if callable(a_object):

            if a_object in self._method_annotations:
                annotation = self._method_annotations[a_object]
                b_object = {
                    "_rtype": "method",
                    "_rtarget": (
                        f"{local_workspace}/{self._client_id}"
                        if local_workspace
                        else self._client_id
                    ),
                    "_rmethod": annotation["method_id"],
                    "_rpromise": True,
                }
            else:
                assert isinstance(session_id, str)
                if hasattr(a_object, "__name__"):
                    object_id = f"{shortuuid.uuid()}-{a_object.__name__}"
                else:
                    object_id = shortuuid.uuid()
                b_object = {
                    "_rtype": "method",
                    "_rtarget": (
                        f"{local_workspace}/{self._client_id}"
                        if local_workspace
                        else self._client_id
                    ),
                    "_rmethod": f"{session_id}.{object_id}",
                    "_rpromise": True,
                }
                store = self._get_session_store(session_id, create=True)
                assert (
                    store is not None
                ), f"Failed to create session store {session_id} due to invalid parent"
                store[object_id] = a_object

            b_object["_rdoc"] = callable_doc(a_object)
            if hasattr(a_object, "__schema__"):
                b_object["_rschema"] = a_object.__schema__
            return b_object

        isarray = isinstance(a_object, list)
        b_object = None

        encoded_obj = None
        for tp in self._codecs:
            codec = self._codecs[tp]
            if codec.encoder and isinstance(a_object, codec.type):
                # TODO: what if multiple encoders found
                encoded_obj = codec.encoder(a_object)
                if isinstance(encoded_obj, dict) and "_rtype" not in encoded_obj:
                    encoded_obj["_rtype"] = codec.name
                # encode the functions in the interface object
                if isinstance(encoded_obj, dict):
                    temp = encoded_obj["_rtype"]
                    del encoded_obj["_rtype"]
                    encoded_obj = self._encode(
                        encoded_obj,
                        session_id=session_id,
                        local_workspace=local_workspace,
                    )
                    encoded_obj["_rtype"] = temp
                b_object = encoded_obj
                return b_object

        if self.NUMPY_MODULE and isinstance(
            a_object, (self.NUMPY_MODULE.ndarray, self.NUMPY_MODULE.generic)
        ):
            v_bytes = a_object.tobytes()
            b_object = {
                "_rtype": "ndarray",
                "_rvalue": v_bytes,
                "_rshape": a_object.shape,
                "_rdtype": str(a_object.dtype),
            }

        elif isinstance(a_object, Exception):
            exc_traceback = "".join(
                traceback.format_exception(
                    type(a_object), value=a_object, tb=a_object.__traceback__
                )
            )
            b_object = {
                "_rtype": "error",
                "_rvalue": str(a_object),
                "_rtrace": exc_traceback,
            }
        elif isinstance(a_object, memoryview):
            b_object = {"_rtype": "memoryview", "_rvalue": a_object.tobytes()}
        elif isinstance(
            a_object, (io.IOBase, io.TextIOBase, io.BufferedIOBase, io.RawIOBase)
        ):
            b_object = {
                m: getattr(a_object, m) for m in IO_PROPS if hasattr(a_object, m)
            }
            b_object["_rtype"] = "iostream"
            b_object["_rnative"] = "py:" + str(type(a_object))
            b_object = self._encode(
                b_object,
                session_id=session_id,
                local_workspace=local_workspace,
            )

        # NOTE: "typedarray" is not used
        elif isinstance(a_object, OrderedDict):
            b_object = {
                "_rtype": "orderedmap",
                "_rvalue": self._encode(
                    list(a_object),
                    session_id=session_id,
                    local_workspace=local_workspace,
                ),
            }
        elif isinstance(a_object, set):
            b_object = {
                "_rtype": "set",
                "_rvalue": self._encode(
                    list(a_object),
                    session_id=session_id,
                    local_workspace=local_workspace,
                ),
            }
        elif isinstance(a_object, (list, dict)):
            keys = range(len(a_object)) if isarray else a_object.keys()
            b_object = [] if isarray else {}
            for key in keys:
                encoded = self._encode(
                    a_object[key],
                    session_id=session_id,
                    local_workspace=local_workspace,
                )
                if isarray:
                    b_object.append(encoded)
                else:
                    b_object[key] = encoded
        else:
            raise Exception(
                "hypha-rpc: Unsupported data type:"
                f" {type(a_object)}, you can register a custom"
                " codec to encode/decode the object."
            )
        return b_object

    def decode(self, a_object):
        """Decode object."""
        return self._decode(a_object)

    def _decode(
        self,
        a_object,
        remote_parent=None,
        local_parent=None,
        remote_workspace=None,
        local_workspace=None,
    ):
        """Decode object."""
        if a_object is None:
            return a_object
        if isinstance(a_object, dict) and "_rtype" in a_object:
            b_object = None
            if (
                self._codecs.get(a_object["_rtype"])
                and self._codecs[a_object["_rtype"]].decoder
            ):
                temp = a_object["_rtype"]
                del a_object["_rtype"]
                a_object = self._decode(
                    a_object,
                    remote_parent=remote_parent,
                    local_parent=local_parent,
                    remote_workspace=remote_workspace,
                    local_workspace=local_workspace,
                )
                a_object["_rtype"] = temp
                b_object = self._codecs[a_object["_rtype"]].decoder(a_object)
            elif a_object["_rtype"] == "method":
                b_object = self._generate_remote_method(
                    a_object,
                    remote_parent=remote_parent,
                    local_parent=local_parent,
                    remote_workspace=remote_workspace,
                    local_workspace=local_workspace,
                )
            elif a_object["_rtype"] == "ndarray":
                # create build array/tensor if used in the plugin
                try:
                    if isinstance(a_object["_rvalue"], (list, tuple)):
                        a_object["_rvalue"] = reduce(
                            (lambda x, y: x + y), a_object["_rvalue"]
                        )
                    # make sure we have bytes instead of memoryview, e.g. for Pyodide
                    elif isinstance(a_object["_rvalue"], memoryview):
                        a_object["_rvalue"] = a_object["_rvalue"].tobytes()
                    elif not isinstance(a_object["_rvalue"], bytes):
                        raise Exception(
                            "Unsupported data type: " + str(type(a_object["_rvalue"]))
                        )
                    if self.NUMPY_MODULE:
                        b_object = self.NUMPY_MODULE.frombuffer(
                            a_object["_rvalue"], dtype=a_object["_rdtype"]
                        ).reshape(tuple(a_object["_rshape"]))

                    else:
                        b_object = a_object
                        logger.warning(
                            "numpy is not available, failed to decode ndarray"
                        )

                except Exception as exc:
                    logger.debug("Error in converting: %s", exc)
                    b_object = a_object
                    raise exc
            elif a_object["_rtype"] == "memoryview":
                b_object = memoryview(a_object["_rvalue"])
            elif a_object["_rtype"] == "iostream":
                b_object = ObjectProxy.fromDict(
                    {
                        k: self._decode(
                            a_object[k],
                            remote_parent=remote_parent,
                            local_parent=local_parent,
                            remote_workspace=remote_workspace,
                            local_workspace=local_workspace,
                        )
                        for k in a_object
                        if not k.startswith("_")
                    }
                )
                b_object["__rpc_object__"] = a_object
            elif a_object["_rtype"] == "typedarray":
                if self.NUMPY_MODULE:
                    b_object = self.NUMPY_MODULE.frombuffer(
                        a_object["_rvalue"], dtype=a_object["_rdtype"]
                    )
                else:
                    b_object = a_object["_rvalue"]
            elif a_object["_rtype"] == "orderedmap":
                b_object = OrderedDict(
                    self._decode(
                        a_object["_rvalue"],
                        remote_parent=remote_parent,
                        local_parent=local_parent,
                        remote_workspace=remote_workspace,
                        local_workspace=local_workspace,
                    )
                )
            elif a_object["_rtype"] == "set":
                b_object = set(
                    self._decode(
                        a_object["_rvalue"],
                        remote_parent=remote_parent,
                        local_parent=local_parent,
                        remote_workspace=remote_workspace,
                        local_workspace=local_workspace,
                    )
                )
            elif a_object["_rtype"] == "error":
                b_object = RemoteException(
                    "RemoteError:"
                    + a_object["_rvalue"]
                    + "\n"
                    + (a_object.get("_rtrace") if a_object.get("_rtrace") else "")
                )
            else:
                # make sure all the interface functions are decoded
                temp = a_object["_rtype"]
                del a_object["_rtype"]
                a_object = self._decode(
                    a_object,
                    remote_parent=remote_parent,
                    local_parent=local_parent,
                    remote_workspace=remote_workspace,
                    local_workspace=local_workspace,
                )
                a_object["_rtype"] = temp
                b_object = a_object
        elif isinstance(a_object, (dict, list, tuple)):
            if isinstance(a_object, tuple):
                a_object = list(a_object)
            isarray = isinstance(a_object, list)
            b_object = [] if isarray else ObjectProxy()
            keys = range(len(a_object)) if isarray else a_object.keys()
            for key in keys:
                val = a_object[key]
                if isarray:
                    b_object.append(
                        self._decode(
                            val,
                            remote_parent=remote_parent,
                            local_parent=local_parent,
                            remote_workspace=remote_workspace,
                            local_workspace=local_workspace,
                        )
                    )
                else:
                    b_object[key] = self._decode(
                        val,
                        remote_parent=remote_parent,
                        local_parent=local_parent,
                        remote_workspace=remote_workspace,
                        local_workspace=local_workspace,
                    )
        # make sure we have bytes instead of memoryview, e.g. for Pyodide
        # elif isinstance(a_object, memoryview):
        #     b_object = a_object.tobytes()
        # elif isinstance(a_object, bytearray):
        #     b_object = bytes(a_object)
        else:
            b_object = a_object
        return b_object
