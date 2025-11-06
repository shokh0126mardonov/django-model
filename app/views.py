from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.urls import reverse

from .models import Task


def home_view(request:HttpRequest)->HttpResponse:
    return render(
        request=request,template_name='home.html'
    )

def create_task(request:HttpRequest)->HttpResponse:
    if request.method == 'GET':
        return render(
            request=request,template_name='task.html'
        )
    elif request.method == 'POST':
        form = request.POST
        new_task = Task(
                title = form.get('title'),
                description = form.get('description'),
                task_level = form.get('task_level')
        )
        new_task.save()
        return redirect(to=reverse('tasks:task_page'))
    

def task_list(request:HttpRequest)->HttpResponse:
    task = Task.objects.all()
    return render(
        request=request,template_name='list.html',context={
            'task':task
        }
    )