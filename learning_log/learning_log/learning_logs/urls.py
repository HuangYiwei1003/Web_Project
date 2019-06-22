"""定义learning_logs的url模式"""

from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    # 主页
    path(r'^index', views.index, name='index'),
    path(r'^topics/', views.topics, name='topics'),
    # 特定页面的详细页面
    path(r'topics/<int:topic_id>/', views.topic, name='topic'),
    # 用于添加新主题的网页
    path(r'^new_topic/$', views.new_topic, name='new_topic'),
    # 用于添加新条目的网页
    path(r'new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # 用于编辑条目的网页
    path(r'edit_entry/<int:entry_id>/$', views.edit_entry, name='edit_entry'),
    # 删除主题
    path(r'delete_topic/<int:topic_id>/$', views.delete_topic, name='delete_topic'),
    # 删除条目
    path(r'delete_entry/<int:entry_id>/$', views.delete_entry, name='delete_entry')
]
