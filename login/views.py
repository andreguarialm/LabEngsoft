from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Teste login")

def login(request):
    return render(request, 'inicial/login.html')

