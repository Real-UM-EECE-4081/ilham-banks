from django.contrib import admin

# Register your models here.

from MyTodoApp.models import Task

admin.site.register(Task)
