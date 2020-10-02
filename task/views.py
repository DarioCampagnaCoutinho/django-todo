from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task
from .forms import TaskForm
import datetime


@login_required
def list(request):
    search = request.GET.get('search')
    filter = request.GET.get('filter')
    tasksDoneRecently = Task.objects.filter(done='done', user=request.user, updated__gt=datetime.datetime.now() - datetime.timedelta(days=30)).count()
    taskDone = Task.objects.filter(done='done', user=request.user).count()
    taskDoing = Task.objects.filter(done='doing', user=request.user).count()
    if search:
        tasks = Task.objects.filter(title__icontains=search, user=request.user)
    elif filter:
        tasks = Task.objects.filter(done=filter, user=request.user)
    else:
        tasks_list = Task.objects.all().order_by('-created').filter(user=request.user)
        paginator = Paginator(tasks_list, 3)
        page = request.GET.get('page')
        tasks = paginator.get_page(page)
    return render(request, 'task/list.html',
                  {'tasks': tasks, 'tasksDoneRecently': tasksDoneRecently,
                   'taskDone': taskDone, 'taskDoing': taskDoing})


@login_required
def detail(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'task/detail.html', {'task': task})


@login_required
def new(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.user = request.user
            task.save()
            messages.info(request, 'Tarefa adicionada com sucesso!')
            return redirect('/')
    else:
        form = TaskForm()
    return render(request, 'task/new.html', {'form': form})


@login_required
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


@login_required
def delete(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    messages.info(request, 'Tarefa excluída com sucesso!')
    return redirect('/')


@login_required
def status(request, id):
    task = get_object_or_404(Task, pk=id)
    if task.done == 'doing':
        task.done = 'done'
    else:
        task.done = 'doing'
    task.save()
    return redirect('/')
