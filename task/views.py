from django.shortcuts import render
from .models import Task


def list(request):
    tasks = Task.objects.all()
    return render(request, 'task/list.html', {'tasks': tasks})
