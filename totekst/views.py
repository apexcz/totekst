from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from . import datastore

from .forms import RegistrationForm,LoginForm,FileUploadForm
# Create your views here.

client  = datastore.create_client('totekst-189610')

def login(request):

    if request.method == 'POST':
        if request.POST['category'] == 'register':
            form = RegistrationForm(request.POST)
            login_form = LoginForm()

            if form.is_valid():

                first_name = form.cleaned_data.get('first_name')
                last_name = form.cleaned_data.get('last_name')
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('new_password')
                confirm_password = form.cleaned_data.get('confirm_password')

                if password != confirm_password:
                    return render(request, 'totekst/login.html')

                user = {'first_name': first_name, 'last_name': last_name, 'email': email, 'password': password}
                datastore.add_user(client=client, dict_user=user)
                return HttpResponseRedirect(reverse('home', args=(email,)))
        elif request.POST['category'] == 'login':
            login_form = LoginForm(request.POST)
            form = RegistrationForm()

            if login_form.is_valid():
                email = login_form.cleaned_data.get('login_email')
                password = login_form.cleaned_data.get('password')
                existing_user = datastore.get_user(client=client,email=email,password=password)

                if existing_user is not None:
                    return HttpResponseRedirect(reverse('home', args=(email,)))
    else:
       form = RegistrationForm()
       login_form = LoginForm()
    return render(request, 'totekst/login.html', {'form': form,'login_form': login_form})

def home(request,email):
    form = FileUploadForm()
    return render(request,'totekst/index.html',{'email':email,'form': form})

def convert(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST,request.FILES)

        if form.is_valid():
            audio = form.cleaned_data.get('audio_file')
            return HttpResponse('File uploaded %d' % audio._size)
        else:
            return render(request, 'totekst/index.html', {'form': form})


def loaderio(request):
    return HttpResponse('loaderio-0138a10a47e6da38eeaa4fd49c2c3670')
    #return HttpResponse(content, content_type='text/plain; charset=utf8')



