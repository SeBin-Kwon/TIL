from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all().order_by('priority')

    context = {
        'todos' : todos,
    }
    return render(request, 'todos/index.html', context)

def create(request):
    content = request.GET.get('content')
    priority = request.GET.get('priority')
    deadline = request.GET.get('deadline')

    Todo.objects.create(content=content,priority=priority,deadline=deadline)
    
    return redirect('todos:index')

def delete(request,pk):
    Todo.objects.get(id=pk).delete()    
    return redirect('todos:index')

def update(request,pk):
    todos = Todo.objects.get(id=pk)
    todos.completed = not todos.completed
    todos.save()
    return redirect('todos:index')

def edit(request,pk):
    todos = Todo.objects.get(id=pk)
    context = {
        'todos' : todos
    }
    return redirect('todos:index', context)

def editUpdate(request,pk):
    todos = Todo.objects.get(id=pk)
    todos.content = request.GET.get('content')
    todos.priority = request.GET.get('priority')
    todos.deadline = request.GET.get('deadline')
    todos.save()
    return redirect('todos:index')