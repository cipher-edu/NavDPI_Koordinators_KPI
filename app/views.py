from django.shortcuts import render, redirect,get_object_or_404,HttpResponseRedirect
from .forms import *
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.utils import timezone
from django.db.models import Count
from django.core.exceptions import ValidationError
@login_required
def home(request):
    user = request.user
    sent_tasks = AddWork.objects.filter(sender=user)
    for task in sent_tasks:
        if task.accepted:
            task.status = True
        else:
            task.status = False
    
    coordinators = Kordinators.objects.annotate(
        num_completed_tasks=Count('taskcompletion')
    )
    
    context = {
        'coordinators': coordinators,
        'sent_tasks': sent_tasks,  # Add the sent tasks to the context
    }

    return render(request, 'glavni.html', context)

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                if user.is_active():
                    login(request, user)
                    return HttpResponse('Muvofaqiyatli krildi')
                
                else:
                    return HttpResponse('Sizni profiliz aktiv emas')
                
            else:
                return HttpResponse('Login va parolda hatolik bor')
    else:
        form = LoginForm()
        context = {
            'form':form
        }
    return render(request, 'registration/login.html', context)

@login_required
def dashboard(request):
    user = request.user
    conetxt = {
        'user':user
    }
    return render(request, 'user_profile.html', conetxt)

class SingUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

@login_required
def kordinators_list(request):
    kordinators = Kordinators.objects.all()
    return render(request, 'kordinators_list.html', {'kordinators': kordinators})

@login_required
def user_profile(request):
    user = request.user  # Get the currently logged-in user
    try:
        kordinator = Kordinators.objects.get(user=user)  # Fetch Kordinators instance related to the user
    except Kordinators.DoesNotExist:
        kordinator = None

    return render(request, 'user_profile.html', {'user': user, 'kordinator': kordinator})
# @login_required
# def update_kordinator_profile(request):
#     user = request.user
#     kordinator = Kordinators.objects.filter(user=user).first()

#     if request.method == 'POST':
#         form = KordinatorsForm(request.POST, request.FILES, instance=kordinator)
#         if form.is_valid():
#             kordinator = form.save(commit=False)
#             kordinator.user = user
#             if 'image' in form.cleaned_data:
#                 kordinator.save()
#                 return redirect('user_profile')
#             else:
#                 form.add_error('image', ValidationError('Please provide an image.'))
#         else:
#             # Handle form validation errors
#             errors = form.errors
#             return render(request, 'update_kordinator_profile.html', {'form': form, 'errors': errors})
#     else:
#         form = KordinatorsForm(instance=kordinator)

#     return render(request, 'update_kordinator_profile.html', {'form': form})

@login_required
def update_kordinator_profile(request):
    user = request.user
    try:
        kordinator = Kordinators.objects.get(user=user)
    except Kordinators.DoesNotExist:
        kordinator = None

    if request.method == 'POST':
        form = KordinatorsForm(request.POST, request.FILES, instance=kordinator)
        if form.is_valid():
            kordinator = form.save(commit=False)
            kordinator.user = user
            kordinator.save()
            return redirect('user_profile')  # Redirect to the user's profile page after saving
    else:
        form = KordinatorsForm(instance=kordinator)

    return render(request, 'update_kordinator_profile.html', {'form': form})

@login_required
def task_list(request):
    tasks = Task.objects.all()
    task_completions = TaskCompletion.objects.filter(coordinator=request.user.kordinators, task__in=tasks)

    task_data = []
    for task in tasks:
        completed = task_completions.filter(task=task).exists()
        is_late_submission = task_completions.filter(task=task, is_late_submission=True).exists()
        task_data.append({'task': task, 'completed': completed, 'is_late_submission': is_late_submission})
    tasks_per_page = 10

    paginator = Paginator(task_data, tasks_per_page)
    page = request.GET.get('page')

    try:
        task_data = paginator.page(page)
    except PageNotAnInteger:
        task_data = paginator.page(1)
    except EmptyPage:
        task_data = paginator.page(paginator.num_pages)

    return render(request, 'task_list.html', {'tasks': task_data})


@login_required
def task_completion(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        form = TaskCompletionForm(request.POST, request.FILES)
        if form.is_valid():

            # Process and save the completion information
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            completed_file = form.cleaned_data['completed_file']
            
            # Calculate lateness based on task_and_date
            is_late_submission = task.task_and_date < timezone.now()

            # Create a TaskCompletion instance and set the is_late_submission field
            coordinator = Kordinators.objects.get(user=request.user)
            task_completion = TaskCompletion(
                task=task,
                coordinator=coordinator,
                title=title,
                description=description,
                completed_file=completed_file,
                is_late_submission=is_late_submission,
            )
            task_completion.save()
            
            return redirect('task_list')  # Redirect to the task list page

    else:
        form = TaskCompletionForm()

    return render(request, 'task_completion.html', {'form': form, 'task': task})



@login_required
def assign_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    coordinators = Kordinators.objects.all()
    
    if request.method == 'POST':
        selected_coordinators = request.POST.getlist('coordinators')
        task.coordinators.add(*selected_coordinators)
        messages.success(request, 'Task assigned successfully.')
        return redirect('task_list')
    
    return render(request, 'assign_task.html', {'task': task, 'coordinators': coordinators})

#vazifalarni qabul qilib olish uchun ishlatish mumkin bo'lgan funksiya
@login_required
def mark_task_received(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    coordinator = get_object_or_404(Kordinators, user=request.user)  # Assuming the coordinator is logged in

    if request.method == 'POST':
        task.mark_as_received(coordinator)
        messages.success(request, 'Task marked as received.')
        return redirect('task_list')

    return render(request, 'mark_task_received.html', {'task': task})


# def task_detail(request, task_id):
#     task = get_object_or_404(Task, id=task_id)

#     if request.method == 'POST':
#         form = TaskCompletionForm(request.POST, request.FILES)
#         if form.is_valid():
#             title = form.cleaned_data['title']
#             description = form.cleaned_data['description']
#             completed_file = form.cleaned_data['completed_file']

#             # Create a TaskCompletion instance and associate it with the task and coordinator
#             coordinator = Kordinators.objects.get(user=request.user)
#             task_completion = TaskCompletion(
#                 task=task,
#                 coordinator=coordinator,
#                 title=title,
#                 description=description,
#                 completed_file=completed_file,
#             )
#             task_completion.save()

#             return redirect('task_list')  # Redirect to the task list page

#     else:
#         form = TaskCompletionForm()

#     return render(request, 'task_detail.html', {'form': form, 'task': task})

@login_required
def task_list(request):
    current_time = timezone.now()
    tasks = Task.objects.all()
    task_completions = TaskCompletion.objects.filter(coordinator=request.user.kordinators, task__in=tasks)
    task_data = []
    for task in tasks:
        completed = task_completions.filter(task=task).exists()
        is_late_submission = task_completions.filter(task=task, is_late_submission=True).exists()

        # Check if the task is overdue
        if task.task_and_date < current_time and not completed:
            is_late_submission = True

        task_data.append({'task': task, 'completed': completed, 'is_late_submission': is_late_submission})

    tasks_per_page = 10


    paginator = Paginator(task_data, tasks_per_page)
    page = request.GET.get('page')

    try:
        task_data = paginator.page(page)
    except PageNotAnInteger:
        task_data = paginator.page(1)
    except EmptyPage:
        task_data = paginator.page(paginator.num_pages)

    return render(request, 'task_list.html', {'tasks': task_data})
##########################################################################################################
@login_required
def send_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        file = request.FILES.get('file')
        sender = request.user  # The sender is the current logged-in user

        task = AddWork(title=title, desc=desc, file=file, sender=sender)
        task.save()

        return redirect('task_list')  # Redirect to the task list page after sending the task

    return render(request, 'send_task.html')

@login_required
def receive_task(request, task_id):
    task = get_object_or_404(AddWork, id=task_id)

    if request.user != task.sender:
        return HttpResponse("You do not have permission to accept this task.")

    # Mark the task as accepted
    task.accepted = True
    task.status = True
    task.save()

    return redirect('task_list')  

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')  # Redirect to a suitable URL after saving the form
    else:
        form = TaskForm()
    
    return render(request, 'task_add.html', {'form': form})