from django import forms

from task_manager.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['text', 'deadline', 'priority']


class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['text', 'deadline',
                  'status', 'priority']
