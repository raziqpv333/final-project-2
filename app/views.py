from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# from .forms import *

# Create your views here.

def function(req):
    return render()
def login(req):
    if 'user' in req.session:
        return redirect(main)
    if req.method=='POST':
        name=req.POST['username']
        password=req.POST['password']
        print(name,password)
        data=authenticate(username=name,password=password)
        print(data)
        if data is not None:
            req.session['user']=name
            print("abc")

            auth_login(req,data)
            return redirect(main)
    return render(req,'main.html')

def main(req):
    if 'user' in req.session:
        a=category.objects.all()
        return render(req,'main.html',{'a':a})
    else:
        return redirect(login)
    
def registration(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        data=User.objects.create_user(first_name=name,email=email,username=username,password=password)
        data.save()
    return render(request,'registration.html')

def contact_view(request):
    return render(request, 'contact.html')


def logout(req):
    if 'user' in req.session:
        auth_logout(req)
        # del req.session
        req.session.flush()
        return redirect(login)
    else:
        return redirect(login)
