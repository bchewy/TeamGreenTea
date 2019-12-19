from django.contrib import admin
# from todolist.models import models
from django.apps import apps

class ListAdminMixin(object):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        super(ListAdminMixin, self).__init__(model, admin_site)
        
models = apps.get_models()
for model in models:
    admin_class = type('AdminClass', (ListAdminMixin, admin.ModelAdmin), {})
    try:
        admin.site.register(model, admin_class)
    except admin.sites.AlreadyRegistered:
        pass

# Register your models here.

# class ItemAdmin(admin.ModelAdmin):
    # pass

# class CategoryAdmin(admin.ModelAdmin):
    # pass
    
# class TodoItemAdmin(admin.ModelAdmin):
    # pass
    
# class TagAdmin(admin.ModelAdmin):
    # pass
    
# admin.site.register(Item, ItemAdmin)
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(TodoItem)
# admin.site.register(Tag)
