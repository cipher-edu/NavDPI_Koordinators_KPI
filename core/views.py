from django.shortcuts import render
from .models import *
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
# Create your views here.
def home(request):
    post = Posts.objects.all()
    contetx = {
        'post':post
    }
    return render(request, 'index.html', contetx)


class TaskAssignmentView(LoginRequiredMixin, View):
    def post(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id)
        task.submission_time = timezone.now()
        task.save()
        return render(request, 'task_assignment_success.html')

class TaskConfirmationView(LoginRequiredMixin, View):
    def post(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id)
        task.is_delayed = False
        task.save()
        return render(request, 'task_confirmation_success.html')

class TaskRejectionView(LoginRequiredMixin, View):
    def post(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id)
        task.delete()
        return render(request, 'task_rejection_success.html')