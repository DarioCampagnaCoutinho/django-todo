from django.shortcuts import render, get_object_or_404
from .models import Task


def list(request):
    tasks = Task.objects.all()
    return render(request, 'task/list.html', {'tasks': tasks})


def detail(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'task/detail.html', {'task': task})


def new(request):
    pass
