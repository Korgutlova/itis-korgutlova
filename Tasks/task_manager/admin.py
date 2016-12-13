from django.contrib import admin

# Register your models here.
from task_manager.models import Task

admin.site.register(Task)