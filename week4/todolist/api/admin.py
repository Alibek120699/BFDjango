from django.contrib import admin

from .models import Task


@admin.register(Task)
class Task(admin.ModelAdmin):
    list_display = ('id', 'title', 'done', 'created_by',)
