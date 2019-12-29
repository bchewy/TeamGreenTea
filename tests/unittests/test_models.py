from django.test import TestCase
from django.contrib.auth.models import User
from todolist.models import *

class TestModels(TestCase):
    def test_tag(self):
        self.tag1 = Tag.objects.create(
            name = 'tag1'
        )
        self.tag2 = Tag.objects.create(
            name = 'tag2'
        )
        admin = User(username='admin', password='testcase', is_superuser=True)
        admin.save()
    
        self.todoitem = TodoItem.objects.create(
            content = 'todoitem',
            created_at = '2019-12-19 18:43',
            updated_at = '2019-12-19 18:43',
            user_id = 1
        )
        
        self.todoitem.tags.add(1)
        self.todoitem.tags.add(2)
        self.assertEquals(self.todoitem.tags.count(), 2)
        
        self.todoitem.tags.clear()
        self.assertEquals(self.todoitem.tags.count(), 0)
