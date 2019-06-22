from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    # 主页
    path(r'', views.homepage, name='homepage'),
]
