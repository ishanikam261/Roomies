from django.shortcuts import render, redirect, get_object_or_404,reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from .models import Task 
from .forms import TaskForm


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'worksheet/task_list.html', {'tasks': tasks})


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('edit')  
    else:
        form = TaskForm()
    return render(request, 'worksheet/create.html', {'form': form})

def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('edit')
    else:
        form = TaskForm(instance=task)
    return render(request, 'worksheet/update.html', {'form': form})
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('edit')
    return render(request, 'worksheet/delete.html', {'task': task})

class adminLoginView(LoginView):
    template_name = "worksheet/login.html"
    form_class = AuthenticationForm
    def get_success_url(self):
        return reverse("edit")
    
def edit(request):
    tasks = Task.objects.all()
    return render(request, 'worksheet/edit.html', {'tasks': tasks})


def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = True
    task.save()
    return redirect('edit')
