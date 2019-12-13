from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=25)

class Item(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='items')

# TodoItem Model
class TodoItem(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class TodoItemArchived(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)