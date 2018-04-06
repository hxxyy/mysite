from django.conf.urls import url
from backend import views
from django.conf.urls import include #添加
urlpatterns = [
    url(r'^$', views.index, name='index'), #链接示例API
]
