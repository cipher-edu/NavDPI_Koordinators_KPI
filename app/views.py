from django.shortcuts import render, redirect
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
