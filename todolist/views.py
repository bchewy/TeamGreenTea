from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import TodoItem, TodoItemArchived, TodoItemLogger
from .models import Tag, TodoItem, TodoItemArchived, TodoItemLogger
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            user.save()
            login(request, user)
            return redirect('/todo/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Todo Items (todoView is the main todo view)
def todoView(request):
    # all_todos_items = TodoItem.objects.all()
    if request.user.is_authenticated:
        all_todos_items = TodoItem.objects.filter(user=request.user)
    else:
        all_todos_items = []
    return render(request, 'todo.html', {'all_items': all_todos_items})

# Creating todoItem
def addTodo(request):
    tagname = request.POST['tag']
    todo_item = TodoItem(content=request.POST['content'], user=request.user)
    todo_item.save()
    for tag in tagname:
        tag = Tag.objects.get(name__exact=tagname)
        todo_item.tags.add(tag.id)
    logger_object = TodoItemLogger(content=todo_item.content, action='A')
    logger_object.save()
    return HttpResponseRedirect('/todo/')

# Deleting todoItem
def deleteTodo(request, pk):
    todo_item = TodoItem.objects.get(id=pk)
    todo_item.delete()
    logger_object = TodoItemLogger(content=todo_item.content, action='D')
    logger_object.save()
    return HttpResponseRedirect('/todo/')


def archiveTodo(request, pk):
    todo_item = TodoItem.objects.get(id=pk)
    todo_content = todo_item.content
    todo_item.delete()
    newArchivedItem = TodoItemArchived(content=todo_content)
    newArchivedItem.save()
    logger_object = TodoItemLogger(content=todo_item.content, action='AR')
    logger_object.save()
    return HttpResponseRedirect('/todo/')

# Updating todoItem
def updateTodo(request, pk):
    todo_item = TodoItem.objects.get(id=pk)
    todo_item.content = request.POST['content']
    # todo_item.tags.set([1])
    tagname = request.POST['tags']
    # tagname = request.POST.get('tags')
    # tagname = "work"
    if tagname == "":
        todo_item.tags.clear()
    else:
        for tag in tagname:
            tag = Tag.objects.get(name__exact=tagname)
            todo_item.tags.add(tag.id)
    # tag = Tag.objects.get(name__exact=tagname)
    # todo_item.tags.set([tag.id])
    # todo_item.tags.add(tag.id)
    logger_object = TodoItemLogger(content=todo_item.content, action='U')
    logger_object.save()
    todo_item.save()
    return HttpResponseRedirect('/todo/')


# Todo Archives
def todoArchived(request):
    all_archived_todos_items = TodoItemArchived.objects.all()
    return render(request, 'todo_archived.html', {'all_items': all_archived_todos_items})


def deleteTodoArchived(request, pk):
    archived_todo = TodoItemArchived.objects.get(id=pk)
    todo_item_content = archived_todo.content
    archived_todo.delete()
    logger_object = TodoItemLogger(content=todo_item_content, action='DA')
    logger_object.save()
    return HttpResponseRedirect('/todoArchived/')


def restoreTodoArchived(request, pk):
    archived_todo = TodoItemArchived.objects.get(id=pk)
    todo_content = archived_todo.content
    newTodo = TodoItem(content=todo_content, user=request.user)
    newTodo.save()
    logger_object = TodoItemLogger(content=todo_content, action='RA')
    logger_object.save()
    archived_todo.delete()
    return HttpResponseRedirect('/todoArchived/')


# Logger
def todoHistoryView(request):
    all_todos_items = TodoItemLogger.objects.all()
    return render(request, 'history.html', {'all_items': all_todos_items})


def todoHistoryClear(request):
    TodoItemLogger.objects.all().delete()
    return HttpResponseRedirect('/todo_history/')


# Others
def todolist_index(request):
    items = Item.objects.all().order_by('-created_on')
    context = {
        "items": items,
    }
    return render(request, "todolist_index.html", context)


def todolist_category(request, category):
    items = Item.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )

    context = {
        "category": category,
        "items": items
    }
    return render(request, "todolist_category.html", context)


def todolist_detail(request, pk):
    item = Item.objects.get(pk=pk)

    context = {
        "item": item,
    }
    return render(request, "todolist_detail.html", context)


# Contributions Page
def todolist_contributions(request):
    return render(request, "todolist_contributions.html")
