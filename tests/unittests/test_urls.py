from django.test import SimpleTestCase
from django.urls import reverse, resolve
from todolist.views import *

class TestUrls(SimpleTestCase):

    def test_index_url(self):
        # assert 1 ==  2
        url = reverse('todolist_index')
        print(resolve(url))
        self.assertEquals(resolve(url).func, todolist_index)
        
    def test_contributions_url(self):
       url = reverse('todolist_contributions')
       print(resolve(url))
       self.assertEquals(resolve(url).func, todolist_contributions)
    
    def test_todo_url(self):
       url = reverse('todoView')
       print(resolve(url))
       self.assertEquals(resolve(url).func, todoView)
    
    def test_addtodo_url(self):
       url = reverse('addTodo')
       print(resolve(url))
       self.assertEquals(resolve(url).func, addTodo)

    def test_deleteTodo_url(self):
       url = reverse('deleteTodo', args=[1])
       print(resolve(url))
       self.assertEquals(resolve(url).func, deleteTodo)
 
    def test_updateTodo_url(self):
       url = reverse('updateTodo', args=[1])
       print(resolve(url))
       self.assertEquals(resolve(url).func, updateTodo)

    def test_todoArchived_url(self):
       url = reverse('todoArchived')
       print(resolve(url))
       self.assertEquals(resolve(url).func, todoArchived)
    
    def test_deleteTodoArchived_url(self):
       url = reverse('deleteTodoArchived', args=[1])
       print(resolve(url))
       self.assertEquals(resolve(url).func, deleteTodoArchived)

    def test_restoreTodoArchived_url(self):
       url = reverse('restoreTodoArchived', args=[0])
       print(resolve(url))
       self.assertEquals(resolve(url).func, restoreTodoArchived)

    def test_todoHistoryView_url(self):
       url = reverse('todoHistoryView')
       print(resolve(url))
       self.assertEquals(resolve(url).func, todoHistoryView)
    
    def test_todoHistoryClear_url(self):
       url = reverse('todoHistoryClear')
       print(resolve(url))
       self.assertEquals(resolve(url).func, todoHistoryClear)