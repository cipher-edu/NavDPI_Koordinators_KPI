from django import forms
from .models import *
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class TaskForm(forms.ModelForm):
    coordinators = forms.ModelMultipleChoiceField(
        queryset=Kordinators.objects.all(), 
        widget=forms.SelectMultiple(attrs={'class': 'select2-selection select2-selection--multiple form-control col-md-6 mb-6'}),
        required=False  
    )
    completed = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'task_name': forms.TextInput(attrs={'class': 'form-control col-md-6 mb-6'}),
            'task_body': forms.Textarea(attrs={'class': 'form-control col-md-6 mb-6'}),
            'task_date': forms.DateInput(attrs={'type': 'datetime-local', 'class': 'form-control col-md-6 mb-6'}),
            'task_and_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control col-md-6 mb-6'}),
        }


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

class QalqonForm(forms.ModelForm):
    class Meta:
        model = Qalqon
        fields = '__all__'
        widgets = {
            'fakultet': forms.Select(attrs={'class':'form-control col-md-12 mb-12'}),
            'yigit_jamoa_soni':forms.NumberInput(attrs={'class':'form-control col-md-12 mb-12'}),
            'qiz_jamoa_soni':forms.NumberInput(attrs={'class':'form-control col-md-12 mb-12'}),
            'all_stat_file':forms.FileInput(attrs={'class':'form-control', 'placeholder': 'agar mavjud bo\'lsa'}),
            }