from django.urls import path

from . import views

urlpatterns = [
    #path("", views.index, name='index'),
    path("", views.todolist_index, name='todolist_index'),
    path("contributions/", views.todolist_contributions, name='todolist_contributions'),
    path("<int:pk>/", views.todolist_detail, name="todolist_detail"),
    path("<category>/", views.todolist_category, name="todolist_category"),
]
