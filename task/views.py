from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Task
from .forms import TaskForm


def list(request):
    search = request.GET.get('search')
    if search:
        tasks = Task.objects.filter(title__icontains=search)
    else:
        tasks_list = Task.objects.all().order_by('-created')
        paginator = Paginator(tasks_list, 3)
        page = request.GET.get('page')
        tasks = paginator.get_page(page)
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
            messages.info(request, 'Tarefa adicionada com sucesso!')
            return redirect('/')
    else:
        form = TaskForm()
    return render(request, 'task/new.html', {'form': form})


def edit(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task.save()
            messages.info(request, 'Tarefa atualizada com sucesso!')
            return redirect('/')
        else:
            return render(request, 'task/edit.html', {'form': form, 'task': task})

    return render(request, 'task/edit.html', {'form': form, 'task': task})


def delete(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    messages.info(request, 'Tarefa excluída com sucesso!')
    return redirect('/')
