from django.contrib import admin
from .models import User, Task

class TaskInline(admin.TabularInline):
    model = Task
    extra = 1

@admin.register(User)
class WorkerAdmin(admin.ModelAdmin):
    inlines = [TaskInline]

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'day', 'task')
    list_filter = ('day',)