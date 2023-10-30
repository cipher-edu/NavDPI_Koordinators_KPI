from django import forms
from .models import *
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class KordinatorsForm(forms.ModelForm):
    class Meta:
        model = Kordinators
        fields = ['name', 'lastname', 'surname', 'age', 'fak', 'ilimiy_darajasi', 'kor_lavozimi', 'tel', 'image', 'about', 'telegram', 'mail']

class TaskCompletionForm(forms.Form):
    title = forms.CharField(
        label='Completion Title',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    description = forms.CharField(
        label='Completion Description',
        widget=forms.Textarea(attrs={'class': 'form-control'}),
    )
    completed_file = forms.FileField(
        label='Attach Completed File (optional)',
        required=False,
    )