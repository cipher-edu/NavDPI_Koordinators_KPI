from django.shortcuts import render
from .models import *
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate
from .forms import *

def home(request):
    post = Posts.objects.all()
    contetx = {
        'post':post
    }
    return render(request, 'index.html', contetx)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page after registration
            return redirect('registration_success')  # Create this URL and view
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})