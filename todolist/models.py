from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


# Create your models here.
# class Category(models.Model):
    # name = models.CharField(max_length=25)

# class Item(models.Model):
    # title = models.CharField(max_length=75)
    # body = models.TextField()
    # created_on = models.DateTimeField(auto_now_add=True)
    # last_modified = models.DateTimeField(auto_now=True)
    # categories = models.ManyToManyField('Category', related_name='items')

# TodoItem Model
class TodoItem(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Tag')
    user = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
      )
    # tags = models.ForeignKey('Tag', on_delete=models.CASCADE)
      
    def __str__(self):
        return self.content

class Tag(models.Model):
    name = models.CharField(max_length=25, unique=True)
    # todoitems = models.ForeignKey('TodoItem', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    # meta API get_field giveup
    def get_field(self):
        return Tag._meta.get_field('name')

# class ItemTag(models.Model):
    # todoitem = models.ForeignKey(TodoItem, on_delete=models.CASCADE)
    # tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

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
    # tags = models.ManyToManyField("Tag")
    action = models.CharField(max_length=1, choices=TYPE) # Can use object.action_display() to show 'Added' instead of 'A' with object.action
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

