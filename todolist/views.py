from django.shortcuts import render
from django.http import HttpResponse
from todolist.models import Item

# Create your views here.
#def index(request):
#  return HttpResponse("Hello, World!")

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
