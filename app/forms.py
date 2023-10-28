from django import forms
from .models import *
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class KordinatorsForm(forms.ModelForm):
    class Meta:
        model = Kordinators
        fields = ['name', 'lastname', 'surname', 'age', 'fak', 'ilimiy_darajasi', 'kor_lavozimi', 'tel', 'image', 'about', 'telegram', 'mail']