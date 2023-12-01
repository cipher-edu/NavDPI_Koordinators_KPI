from django import forms
from .models import *
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
class KordinatorsForm(forms.ModelForm):
    class Meta:
        model = Kordinators
        exclude = ['user']
        # fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control col-md-12 mb-12'}),
            'lastname': forms.TextInput(attrs={'class':'form-control col-md-12 mb-12'}), 
            'surname': forms.TextInput(attrs={'class':'form-control col-md-12 mb-12'}),
            'age': forms.NumberInput(attrs={'class':'form-control col-md-12 mb-12'}),
            'fak': forms.Select(attrs={'class':'form-control col-md-12 mb-12'}),
            'ilimiy_darajasi': forms.Select(attrs={'class':'form-control col-md-12 mb-12'}),
            'kor_lavozimi': forms.Select(attrs={'class':'form-control col-md-12 mb-12'}),
            'tel': forms.TextInput(attrs={'class':'form-control col-md-12 mb-12'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),
            'about': forms.TextInput(attrs={'class':'form-control col-md-12 mb-12'}),
            'telegram': forms.TextInput(attrs={'class':'form-control col-md-12 mb-12'}),
            'mail': forms.TextInput(attrs={'class':'form-control col-md-12 mb-12'}),
        }
class TaskCompletionForm(forms.Form):
    title = forms.CharField(
        label='Topshiriq sarlavhasi',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control col-md-4'}),
    )
    description = forms.CharField(
        label='Topshiriq haqida',
        widget=forms.Textarea(attrs={'class': 'form-control col-md-4'}),
    )
    completed_file = forms.FileField(
        label='Topshirirqning bayonnomasi (jpg, pdf, word, excel)',
        required=False,
    )