from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


def sign_in (request):
    if request.method =='GET':
        form=LoginForm()
        context={'form':form}
        return render(request,'user/login_user.html',context)
    
    elif request.method =='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request,f'{username.title()}, welcome back !')
                return redirect('store:index')
            
    # either form not valid or user is not authenticated
    messages.error(request,f'Invalid username or password')
    return render(request,'user/loin_user.html',context)        


def sign_out(request):
    logout(request)
    return redirect('store:index')

def register_user(request):
    if request.method=='GET':
       form=SigupForm()
       context={'form':form}
       return render(request,'user/register_user.html',context)
    elif request.method =='POST':
        form=SigupForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            messages.success(request,'You have siguned up successfully')
            login(request,user)
            return redirect('store:index')
        else:
            context={'form':form}
            return render(request,'user/register_user.html',context)

