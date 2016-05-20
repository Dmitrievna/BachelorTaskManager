from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.all_tasks, name = 'all_tasks'),
    url(r'^task/(?P<pk>[0-9]+)/$', views.view_task, name = 'view_task'),
    url(r'^task/new/$', views.add_task, name = 'add_task'),
    url(r'^get_name/', views.get_name, name = 'name'),




]