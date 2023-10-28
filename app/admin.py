from django.contrib import admin
from .models import * 
# Register your models here.


# admin.site.register(UserProfile)
admin.site.register(Kordinators)


class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'task_body', 'task_date','task_and_date','task_file', 'id',)
admin.site.register(Task, TaskAdmin)