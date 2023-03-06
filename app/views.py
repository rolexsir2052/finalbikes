from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from app.models import *
# Create your views here.
@login_required(login_url='login_page')
def home(request):
    return render(request,'home.html')
def register(request):
    if request.method=='POST':
        N=request.POST.get('n')
        P=request.POST.get('p')
        U=User.objects.create_user(username=N,password=P)
        U.save()
        return redirect('home')
    return render(request,'register.html')
def contact(request):
    if request.method=='POST':
        names=request.POST.get('n')
        e=request.POST.get('e')
        m=request.POST.get('m')
        C=Contact.objects.get_or_create(name=names,email=e,message=m)[0]
        C.save()
        return redirect('home')
    return render(request,'contact.html')
def login_page(request):
    if request.method=='POST':
        N=request.POST.get('n')
        P=request.POST.get('p')
        user=authenticate(username=N,password=P)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('login_page')
    return render(request,'login_page.html')
def logout_user(request):
    logout(request)
    return redirect('login_page')
