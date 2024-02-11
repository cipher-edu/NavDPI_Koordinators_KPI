from django.contrib import admin
from .models import * 
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils.safestring import mark_safe
from django.db.models import Count 
from django.contrib import messages
from django.db.models import Sum
# Register your models here.


# admin.site.register(UserProfile)

@admin.register(Kordinators)
class KordinatorsAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'lastname', 'surname', 'display_image')
    list_filter = ('user', 'name', 'lastname', 'surname',)
    search_fields = ('user', 'name', 'lastname', 'surname',)
    list_display_links = ('user',)
    # list_editable = ('JSHSHIR', 'passport')

    def display_image(self, objectcha):
        return mark_safe(f"<img src='{objectcha.image.url}' width='150' height='150' /> ")


@admin.register(Task)
class TaskAmdin(admin.ModelAdmin):
    list_display = ('task_name', 'task_body', 'task_date', 'task_and_date',  'task_file',)
    list_filter = ('task_name', 'task_body', 'task_date', 'task_and_date', 'coordinators',)
    search_fields = ('task_name', 'task_body', 'task_date', 'task_and_date', 'coordinators',)
    list_display_links = ('task_name',)
@admin.register(TaskCompletion)
class TaskCompletionAdmin(admin.ModelAdmin):
    list_display = ('task', 'completion_date', 'title', 'description', 'completed_file', 'is_late_submission')
    list_filter = ('task', 'completion_date', 'title', 'description', 'completed_file', 'is_late_submission')
    search_fields = ('task', 'completion_date', 'title', 'description', 'completed_file', 'is_late_submission')
    list_display_links = ('task',)

    def get_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ('task', 'coordinator', 'title', 'description', 'completed_file', 'is_late_submission', 'completed')
        return ('task', 'title', 'description', 'completed_file')

    def save_model(self, request, obj, form, change):
        if not obj.coordinator_id:
            coordinators = Kordinators.objects.annotate(num_tasks=Count('taskcompletion')).order_by('num_tasks')
            if coordinators.exists():
                obj.coordinator = coordinators.first()
            else:
                raise IntegrityError("No available coordinator found.")
        
        super().save_model(request, obj, form, change)
        
        if obj.coordinator:
            message_text = f"Task '{obj.task}' completed successfully."
            messages.add_message(request, messages.INFO, message_text)

@admin.register(AddWork)
class AddWorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'file', 'sender_name', 'accepted')
    list_filter = ('accepted','sender')
    search_fields = ('title', 'desc', 'sender__username')

    def get_exclude(self, request, obj=None):
        if not request.user.is_superuser:
            return ['sender', 'accepted']
        return []

    def save_model(self, request, obj, form, change):
        if not obj.sender_id:
            obj.sender = request.user
        super().save_model(request, obj, form, change)

    def sender_name(self, obj):
        return obj.sender.get_full_name() or obj.sender.username
    sender_name.short_description = 'Yuboruvchi'

@admin.register(Qalqon)
class QalqonAdmin(admin.ModelAdmin):
    list_display = ('fakultet', 'yigit_jamoa_soni', 'qiz_jamoa_soni', 'all_stat_file',)
    list_filter = ('fakultet', 'yigit_jamoa_soni', 'qiz_jamoa_soni')
    search_fields = ('fakultet', 'yigit_jamoa_soni', 'qiz_jamoa_soni')

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        
        # Save the object
        super().save_model(request, obj, form, change)
        message_text = f"New Qalqon data added by {obj.user.username}."
        messages.add_message(request, messages.INFO, message_text)

@admin.register(Tavsiyanoma)
class TavsiyanomaAdmin(admin.ModelAdmin):
    list_display = ('fakultet', 'yigit_jamoa_soni', 'qiz_jamoa_soni', 'all_stat_file',)
    list_filter = ('fakultet', 'yigit_jamoa_soni', 'qiz_jamoa_soni')
    search_fields = ('fakultet', 'yigit_jamoa_soni', 'qiz_jamoa_soni')

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        
        # Save the object
        super().save_model(request, obj, form, change)
        message_text = f"New Qalqon data added by {obj.user.username}."
        messages.add_message(request, messages.INFO, message_text)

@admin.register(Utizbeshfoiz)
class UtizbeshfoizAdmin(admin.ModelAdmin):
    list_display = ('fakultet', 'yigit_jamoa_soni', 'qiz_jamoa_soni', 'all_stat_file',)
    list_filter = ('fakultet', 'yigit_jamoa_soni', 'qiz_jamoa_soni')
    search_fields = ('fakultet', 'yigit_jamoa_soni', 'qiz_jamoa_soni')

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        
        # Save the object
        super().save_model(request, obj, form, change)
        message_text = f"New Qalqon data added by {obj.user.username}."
        messages.add_message(request, messages.INFO, message_text)
