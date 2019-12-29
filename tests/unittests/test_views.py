from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from todolist.models import *
import json
# from django.utils import timezone

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()        
        self.todo_url = reverse('todoView')
        self.addTodo = reverse('addTodo')
        
        admin = User(username='admin', password='testcase', is_superuser=True)
        admin.save()
        me = User.objects.get(username='admin')
        assert me.is_superuser
        
        Tag.objects.create(
            name='self'
        )

    def test_todoView(self):
        response = self.client.get(reverse('todoView'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo.html')

    # def test_addTodo(self):
        # admin2 = User(username='admin2', password='testcase', is_superuser=True)
        # admin2.save()
        # user2 = User.objects.get(username='admin2')
        
        # response = self.client.post(self.addTodo, {
            # 'content' : 'todoitem',
            # 'created_at' : '2019-12-19 18:43',
            # 'updated_at' : '2019-12-19 18:43',
            # 'tag' :  '',
            # 'user' :  user2
        # })
        # self.assertEquals(response.status_code, 302)

    # def test_addTodo_nodata(self):
        # response = self.client.post(self.addTodo), {
        # 'tag' : 'self'
        # }
        # self.assertEquals(response.status_code, 302)
        # self.assertEquals(self.todoitem.tag.count(),0)