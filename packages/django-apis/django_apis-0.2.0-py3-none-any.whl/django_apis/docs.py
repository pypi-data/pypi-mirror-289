import re
import typing
import inspect

import pydantic
from zenutils import treeutils

from django.conf import settings
from django.utils.translation import gettext
from django.apps import apps
from django.urls import resolve
from django.urls import reverse
from django.urls import get_resolver
from django.core.files.uploadedfile import UploadedFile

from .constants import DJANGO_APIS_METHODS_KEY
from .constants import DJANGO_APIS_OPENAPI_SERVERS_KEY
from .constants import DJANGO_APIS_OPENAPI_SERVERS_DEFAULT
from .constants import DJANGO_APIS_VIWE_FLAG_KEY
from .constants import DJANGO_APIS_OPENAPI_TITLE_KEY
from .constants import DJANGO_APIS_OPENAPI_VERSION_KEY
from .constants import DJANGO_APIS_OPENAPI_VERSION_DEFAULT
from .constants import DJANGO_APIS_OPENAPI_DESCRIPTION_KEY
from .constants import DJANGO_APIS_OPENAPI_DESCRIPTION_DEFAULT
from .views import DJANGO_APIS_BASE_RESPONSE_CLASS


def get_default_title():
    """获取默认的工程名称。"""
    return settings.ROOT_URLCONF.split(".")[0]


def is_django_apis_view(view):
    """判断视图函数是否为使用`django-apis`提供的`apiview`方法注解的函数。"""
    return getattr(
        view,
        DJANGO_APIS_VIWE_FLAG_KEY,
        False,
    )


def get_tags_mapping():
    """创建应用标签查询表。"""
    modules_mapping = treeutils.SimpleRouterTree()
    for app in apps.get_app_configs():
        modules_mapping.index(app.module.__spec__.name, app.label)
    return modules_mapping


def get_tags_from_paths(paths):
    """获取所有提供了接口的应用标签列表。"""
    all_tags = []
    for path, path_info in paths.items():
        for method, method_info in path_info.items():
            tags = set(method_info.get("tags", []))
            all_tags += tags
    return set(all_tags)


def get_tags(paths):
    """获取全局应用标签信息列表。"""
    all_tags = get_tags_from_paths(paths)
    tags = []
    for app in apps.get_app_configs():
        tag_name = app.label
        if not tag_name in all_tags:
            continue
        tag = {}
        tag["name"] = tag_name
        tag["description"] = gettext(app.verbose_name)
        tags.append(tag)
    return tags


def get_simple_type(type):
    """处理简单参数类型的定义。"""
    if issubclass(type, str):
        return {"type": "string"}
    elif issubclass(type, int):
        return {"type": "integer"}
    elif issubclass(type, float):
        return {"type": "number"}
    else:
        return {}


def get_view_summary(view_doc):
    """把视图详细说明中的第一行作为视图名称。"""
    return view_doc.splitlines()[0]


def get_view_methods(view):
    """从视图函数中获取视图支持的HTTP请求方法列表。"""
    return getattr(
        view,
        DJANGO_APIS_METHODS_KEY,
        ["GET"],
    )


def format_tags(tags):
    """格式化标签。总是为字符串数组。"""
    if isinstance(tags, str):
        return [tags]
    elif isinstance(tags, (list, set, tuple)):
        tags = list(tags)
        tags.sort()
        return tags
    else:
        return []


def has_file_field(parameter_info):
    """判断当前接口是否需要上传文件。"""
    if parameter_info.annotation == inspect._empty:
        return False
    return '"binary"' in parameter_info.annotation.schema_json()


def get_view_schema(view, tags=None):
    """获取视图定义。"""
    schema = {}
    description = view.__doc__ or ""
    info = {
        "summary": description and description.splitlines()[0] or "",
        "description": description,
        "tags": format_tags(tags),
    }
    signature = inspect.signature(view)
    for parameter_name, parameter_info in signature.parameters.items():
        # 处理json payload请求体
        if parameter_name == "payload":
            info["requestBody"] = {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": (parameter_info.annotation != inspect._empty)
                        and parameter_info.annotation.schema()
                        or {},
                    },
                },
            }
        # 处理表单请求体
        elif parameter_name == "form":
            mimetype = "application/x-www-form-urlencoded"
            if has_file_field(parameter_info):
                mimetype = "multipart/form-data"

            info["requestBody"] = {
                "required": True,
                "content": {
                    mimetype: {
                        "schema": (parameter_info.annotation != inspect._empty)
                        and parameter_info.annotation.schema()
                        or {},
                    },
                },
            }
        # 处理url参数
        elif parameter_name == "query":
            if not "parameters" in info:
                info["parameters"] = []
            info["parameters"] += (
                (parameter_info.annotation != inspect._empty)
                and get_query_parameters(parameter_info.annotation.schema())
                or []
            )
        # @todo: 添加headers, cookies参数支持
        # 处理path参数
        else:
            if not "parameters" in info:
                info["parameters"] = []
            info["parameters"] += get_path_parameters(parameter_name, parameter_info)
    # 处理响应体
    info["responses"] = {
        "200": {
            "description": "Success",
            "content": {
                "application/json": {
                    "schema": get_response_schema(signature.return_annotation),
                }
            },
        }
    }
    # 为每种支持的请求方法生成接口定义
    methods = get_view_methods(view)
    for method in methods:
        schema[method.lower()] = info
    return schema


def get_response_schema(type_class):
    """获得接口响应数据模型。"""
    if type_class == inspect._empty:
        return {}
    elif type(type_class) == typing._GenericAlias:
        return make_generic_response_type(
            type_class,
        )
    elif issubclass(type_class, pydantic.BaseModel):
        return type_class.schema()
    else:
        return make_generic_response_type(
            type_class,
        )


def make_generic_response_type(type_class):
    """构建接口响应数据模型。"""

    class _ResponseType(DJANGO_APIS_BASE_RESPONSE_CLASS):
        data: type_class

    return _ResponseType.schema()


def get_query_parameters(query_schema):
    """获取url参数定义。"""
    parameters = []
    required = query_schema.get("required", [])
    for prop_name, prop_info in query_schema["properties"].items():
        parameters.append(
            {
                "in": "query",
                "name": prop_name,
                "description": prop_info.get("description", prop_info.get("title", "")),
                "schema": {"type": prop_info["type"]},
                "required": prop_name in required,
            }
        )
    return parameters


def get_path_parameters(parameter_name, parameter_info):
    """获取路径参数定义。"""
    return [
        {
            "in": "path",
            "name": parameter_name,
            "schema": get_simple_type(parameter_info.annotation),
            "required": True,
        }
    ]


def get_paths():
    """获取所有接口定义。"""
    paths = {}
    tags_mapping = get_tags_mapping()
    global_urls = get_resolver().reverse_dict
    for view_item in global_urls.lists():
        # 获取当前视图的的处理函数
        view_func = view_item[0]
        if isinstance(view_func, str):
            try:
                view_func = resolve(reverse(view_func)).func
            except Exception:
                continue
        # 如果不是django-apis视图，则忽略
        if not is_django_apis_view(view_func):
            continue
        # 查找到当前视图函数所在应用标签，作为本接口的tag_name
        tag_name, _ = tags_mapping.get_best_match(view_func.__module__)
        if not tag_name:
            tag_name = "__all__"
        # 遍历所有视图公开的paths
        view_paths = view_item[1]
        for view_path in view_paths:
            path = "/" + view_path[0][0][0]
            path = re.sub("\\%\\(([^\\)]*)\\)s", "{\\1}", path)
            paths[path] = get_view_schema(view_func, tag_name)
    return paths


def get_docs():
    """获取swagger数据。"""
    paths = get_paths()
    tags = get_tags(paths)
    return {
        "openapi": "3.0.0",
        "servers": getattr(
            settings,
            DJANGO_APIS_OPENAPI_SERVERS_KEY,
            DJANGO_APIS_OPENAPI_SERVERS_DEFAULT,
        ),
        "info": {
            "title": getattr(
                settings,
                DJANGO_APIS_OPENAPI_TITLE_KEY,
                get_default_title(),
            ),
            "version": getattr(
                settings,
                DJANGO_APIS_OPENAPI_VERSION_KEY,
                DJANGO_APIS_OPENAPI_VERSION_DEFAULT,
            ),
            "description": getattr(
                settings,
                DJANGO_APIS_OPENAPI_DESCRIPTION_KEY,
                DJANGO_APIS_OPENAPI_DESCRIPTION_DEFAULT,
            ),
        },
        "tags": tags,
        "paths": paths,
        "components": {},
        "security": [],
    }
