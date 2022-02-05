from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    user={'name':'Rakesh','age':25,'city':'Pune'}
    return render(request, 'home.html',user)

def info(request):
    user={'name':'Ram','age':30,'city':'Mumbai'}
    return render(request, 'info.html',user)

