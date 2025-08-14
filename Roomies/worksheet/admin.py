from django.contrib import admin
from .models import User, Task

class TaskInline(admin.TabularInline):
   pass

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
   pass

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'day', 'task')
    list_filter = ('day',)