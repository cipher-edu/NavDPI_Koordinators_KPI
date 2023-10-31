from django.shortcuts import render, redirect,get_object_or_404
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
@login_required
def home(request):
    return render(request, 'index.html')


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

# task list
@login_required
def task_list(request):
    tasks = Task.objects.all()
    task_completions = TaskCompletion.objects.filter(coordinator=request.user.kordinators, task__in=tasks)

    task_data = []
    for task in tasks:
        completed = task_completions.filter(task=task).exists()
        task_data.append({'task': task, 'completed': completed})

    return render(request, 'task_list.html', {'tasks': task_data})
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
# @login_required
# def mark_task_received(request, task_id):
#     task = get_object_or_404(Task, id=task_id)
#     coordinator = get_object_or_404(Kordinators, user=request.user)  # Assuming the coordinator is logged in

#     if request.method == 'POST':
#         task.mark_as_received(coordinator)
#         messages.success(request, 'Task marked as received.')
#         return redirect('task_list')

#     return render(request, 'mark_task_received.html', {'task': task})


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
def task_completion(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    coordinator = Kordinators.objects.get(user=request.user)

    # Check if a TaskCompletion instance already exists for the task and coordinator
    existing_completion = TaskCompletion.objects.filter(task=task, coordinator=coordinator).first()

    if existing_completion:
        # A completion for this task by this coordinator already exists
        return HttpResponse("You have already completed this task.")

    if request.method == 'POST':
        form = TaskCompletionForm(request.POST, request.FILES)
        if form.is_valid():
            # Process and save the completion information
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            completed_file = form.cleaned_data['completed_file']

            # Create a TaskCompletion instance and associate it with the task and coordinator
            task_completion = TaskCompletion(
                task=task,
                coordinator=coordinator,
                title=title,
                description=description,
                completed_file=completed_file,
            )
            task_completion.save()
            return redirect('task_list')  # Redirect to the task list page

    else:
        form = TaskCompletionForm()

    return render(request, 'task_completion.html', {'form': form, 'task': task})

