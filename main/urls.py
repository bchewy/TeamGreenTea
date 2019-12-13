"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from todolist.views import todoView, addTodo, deleteTodo, updateTodo, todoArchived, deleteTodoArchived, restoreTodoArchived, archiveTodo, todoHistoryView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("todolist/", include("todolist.urls")),
    # Routes for todos
    path("todo/", todoView),
    path("addTodo/", addTodo),
    path("deleteTodo/<int:pk>/", deleteTodo),
    path("updateTodo/<int:pk>/", updateTodo),
    # Routes for todo archives
    path("todoArchived/", todoArchived),
    path("archiveTodo/<int:pk>/", archiveTodo),
    path("deleteArchive/<int:pk>/", deleteTodoArchived),
    path("restoreArchive/<int:pk>/", restoreTodoArchived),
    # Routes for history/logging
    path("todo_history/", todoHistoryView),


]
