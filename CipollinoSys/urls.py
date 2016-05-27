from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^all_tasks/$', views.all_tasks, name = 'all_tasks'),
    url(r'^task/(?P<pk>[0-9]+)/$', views.view_task, name = 'view_task'),
    url(r'^task/new/$', views.add_task, name = 'add_task'),
    url(r'^task/(?P<pk>[0-9]+)/edit/$', views.edit_task, name='edit_task'),
    url(r'^error/$', views.error, name = 'error'),
    url(r'^$', views.log_in, name = 'log_in'),
    url(r'^users/$', views.users, name = 'users'),
    url(r'^user/(?P<pk>[0-9]+)/view_statistic/$', views.view_statistic, name='view_statistic'),
    url(r'^task_stat/$', views.task_stat, name = 'task_stat'),




]