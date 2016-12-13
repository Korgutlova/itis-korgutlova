from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect as Redirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from task_manager.forms import TaskForm, EditTaskForm
from task_manager.models import Task


def show_tasks(request):
    # task_list = Task.objects.values_list("text", flat=True)
    # result = "<br>".join(task_list)

    # task_list = Task.objects.filter(priority=100)

    # task_list = Task.objects.filter(priority__gt=2)

    # task_list = Task.objects.filter(text__contains="ea")

    # task_list = Task.objects.exclude(priority=100)
    # result = "<br>".join([task.__str__() for task in task_list])

    # q1 = Q(text__contains="mm")
    # q2 = Q(priority__gt=7)
    # q = q1 | q2
    # task_list = Task.objects.filter(q)

    # task_list = Task.objects.all()
    # result = "<br>".join([task.__str__() for task in task_list])
    # return HttpResponse(result)
    return render(request,
                  "task_manager/all_tasks.html",
                  {"tasks": Task.objects.all()})

def show_task(request, task_id):
    t = Task.objects.get(id=task_id)
    return HttpResponse("<h1>Task: [ %s ]</h1>" % t)


def create_task(request):
    context = {}
    if 'text' in request.POST:
        f = TaskForm(request.POST)
        f.save()
        context["result"] = "Task created"
        return Redirect(reverse("tasks:all"))
    context["form"] = TaskForm()
    return render(request, "task_manager/create.html", context)


def edit_task(request, task_id):
    if request.method == "POST":
        task = Task.objects.get(id=task_id)
        f = EditTaskForm(request.POST, instance=task)
        f.save()
        return Redirect(reverse("tasks:all"))

    elif request.method == "GET":
        task = Task.objects.get(id=task_id)
        f = EditTaskForm(instance=task)
        return render(request,
                      "task_manager/edit.html",
                      {"form": f})
    else:
        return HttpResponse("Method is not supported")