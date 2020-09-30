from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm


def list(request):
    tasks = Task.objects.all().order_by('-created')
    return render(request, 'task/list.html', {'tasks': tasks})


def detail(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'task/detail.html', {'task': task})


def new(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.save()
            return redirect('/')
    else:
        form = TaskForm()
    return render(request, 'task/new.html', {'form': form})
