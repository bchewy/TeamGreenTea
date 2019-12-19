from django.contrib import admin
from todolist.models import Category, Item, TodoItem

# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(TodoItem)
