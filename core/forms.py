from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # Import your custom user model

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = CustomUser  # Replace with your custom user model
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')
