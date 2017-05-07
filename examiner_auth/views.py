from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout

from models import UserProfile

def user_register(request) : 
    return redirect('/')

def user_logout(request) : 
    logout(request)
    return redirect('/')    

def user_login(request) : 
    user = authenticate(username = request.POST.get('username', ''), \
        password = request.POST.get('password', ''))
    if user is not None : 
        if user.is_active : 
            login(request, user)
            return render(request, 'home.html')
        else : 
            pass
            # this account is disabled
    return render(request, 'login.html')
    # else : 
    #     return redirect('/accounts/register/')