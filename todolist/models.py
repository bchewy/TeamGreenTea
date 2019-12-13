from django.db import models
from django.utils import timezone

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
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Tag')

class Tag(models.Model):
    name = models.CharField(max_length=25)

class TodoItemArchived(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

class TodoItemLogger(models.Model):
    TYPE = (
        ('A','Added'),
        ('D','Deleted'),
        ('U','Updated'),
        ('AR','Archived'), # Archived a todoitem object
        ('DA','Deleted Archive'), # Deleted an archive object
        ('RA','Restored Archive'), # Restored a todoitem
    )
    content = models.TextField()
    action = models.CharField(max_length=1, choices=TYPE) # Can use object.action_display() to show 'Added' instead of 'A' with object.action
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

