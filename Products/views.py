from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello")

def Home(request):
    return render (request,'home.html')

def Signup(request):
    return render(request,'signup.html')

def Login(request):
    return render (request,'login.html')