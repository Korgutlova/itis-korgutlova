from django.conf.urls import url

from task_manager.views import *

urlpatterns = [
    url(r'^all$', show_tasks, name="all"),
    url(r'^(?P<task_id>\d+)$', show_task),
    url(r'^(?P<task_id>\d+)/edit', edit_task, name="edit_task"),
    url(r'^create$', create_task),
]
