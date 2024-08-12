# django-apis

Django简易json api接口框架。使用`pydantic`做接口参数验证。


## 安装

```
pip install django-apis
```

## 配置项

- DJANGO_APIS_BASE_RESPONSE_CLASS: 通用的接口响应模型
- DJANGO_APIS_OPENAPI_SERVERS: Swagger服务器列表
- DJANGO_APIS_OPENAPI_TITLE: Swagger标题
- DJANGO_APIS_OPENAPI_VERSION: Swagger版本号
- DJANGO_APIS_OPENAPI_DESCRIPTION: Swagger描述

## 使用案例

```python
import pydantic
from django_apis.views import apiview
from django_apis.schemas import OptionalUploadedFile

@apiview()
def ping() -> str:
    return "pong"


class EchoPayload(pydantic.BaseMode):
    msg: str

@apiview(methods="post")
def echo(payload: EchoPayload) -> str:
    return payload.msg

class ApplyForm(pydantic.BaseMode):
    name: str
    start_date: str
    end_date: str
    files: List[OptionalUploadedFile]

@apiview(methods="post")
def apply(form: ApplyForm) -> bool:
    return True

```

## 版本记录

### v0.2.0

- 注意：不兼容0.1.x。

