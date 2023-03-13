from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.core.mail import send_mail

def home(request):
    return render(request, 'website/index.html')