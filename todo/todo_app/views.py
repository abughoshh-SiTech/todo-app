from django.shortcuts import render, redirect
from .models import Task
from .forms import TasksForm
from django.contrib import messages


def home(request):

    if request.method == 'POST':
        form = TasksForm(request.POST or None)

        if form.is_valid():
            form.save()
            Tasks = Task.objects.all
            messages.success(request, ('Task Has been added!'))
            return render(request, 'home.html', {'Tasks': Tasks})

    else:
        Tasks = Task.objects.all
        return render(request, 'home.html', {'Tasks': Tasks})


def delete(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    messages.success(request, ('Task Has been deleted!'))

    return redirect('home')

def complete(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.done = True
    task.save()
    messages.success(request, ('Task Has been completed!'))
    return redirect('home')

def uncomplete(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.done = False
    task.save()
    messages.success(request, ('Task Has been uncompleted!'))
    return redirect('home')


def edit(request, task_id):
    if request.method == 'POST':
        task = Task.objects.get(pk=task_id)

        form = TasksForm(request.POST or None, instance = task)

        if form.is_valid():
            form.save()
            messages.success(request, ('Task Has been edited!'))
            return redirect('home')

    else:
        task = Task.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task': task})
