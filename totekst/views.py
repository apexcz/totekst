from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def login(request):
    return render(request,'totekst/login.html')

def login_post(request):
    email = request.POST['email']
    password = request.POST['password']

    return HttpResponseRedirect(reverse('totekst:home',args=(email,)))

def home(request,email):
    return render(request,'totekst/index.html',{'email':email})


