from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone 
from django.contrib.auth.models import User 
# Create your views here.

def index(request):
    return render(request, 'index.html')
    
def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')