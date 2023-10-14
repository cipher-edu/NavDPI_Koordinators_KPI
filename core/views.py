from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    post = Posts.objects.all()
    contetx = {
        'post':post
    }
    return render(request, 'index1.html', contetx)