from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import TodoItem, Item

# Todo Items (todoView is the main todo view)
def todoView(request):
    all_todos_items = TodoItem.objects.all()
    return render(request, 'todo.html', {'all_items':all_todos_items})

# Creating todoItem
def addTodo(request):
    newTodo = TodoItem(content = request.POST['content'])
    newTodo.save()
    return HttpResponseRedirect('/todo/')

# Deleting todoItem
def deleteTodo(request, todo_id):
    todo_item = TodoItem.objects.get(id = todo_id)
    todo_item.delete()
    return HttpResponseRedirect('/todo/')

# Updating todoItem
def updateTodo(request, todo_id):
    todo_item = TodoItem.objects.get(id = todo_id)
    todo_item.content = request.POST['content']
    todo_item.save()
    return HttpResponseRedirect('/todo/')

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