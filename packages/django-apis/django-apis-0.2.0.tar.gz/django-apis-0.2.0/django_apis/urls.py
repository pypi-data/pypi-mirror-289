from django.urls import path
from . import swagger_ui

urlpatterns = [
    path(
        "docs/",
        swagger_ui.swagger_ui_view,
        name="django_apis_swagger_ui_view",
    ),
    path(
        "docs/init.js",
        swagger_ui.swagger_ui_init_js,
        name="django_apis_swagger_ui_init_js",
    ),
    path(
        "docs/data.json",
        swagger_ui.swagger_ui_data,
        name="django_apis_swagger_ui_data",
    ),
]
