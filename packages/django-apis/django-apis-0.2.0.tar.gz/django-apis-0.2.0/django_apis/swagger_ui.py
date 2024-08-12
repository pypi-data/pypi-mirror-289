from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .docs import get_docs


@login_required(login_url=reverse_lazy("admin:index"))
def swagger_ui_view(request):
    """SWAGGER-UI管理界面。"""
    return render(
        request,
        "django_apis/swagger_ui.html",
        {},
    )


@login_required(login_url=reverse_lazy("admin:index"))
def swagger_ui_data(request):
    """SWAGGER-UI数据接口。"""
    docs = get_docs()
    return JsonResponse(
        docs,
        json_dumps_params={
            "ensure_ascii": False,
        },
    )


@login_required(login_url=reverse_lazy("admin:index"))
def swagger_ui_init_js(request):
    """SWAGGER-UI JS脚本。"""
    return render(
        request,
        "django_apis/swagger_ui_init.js",
        {},
        content_type="application/javascript",
    )
