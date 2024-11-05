from django.contrib import admin
from todo.models import TodoItem


class TodoAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "completed", "created_at"]


admin.site.register(TodoItem, TodoAdmin)
