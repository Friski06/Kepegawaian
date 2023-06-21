from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from .forms import FromLogin


# Create your views here.

def login(request):

    form = FromLogin()
    if request.method == 'POST':    
        username = request.POST['username']
        password = request.POST['password']


        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html', {'form':form})


def register(request):
    kontext = {}
    return render(request, 'register.html', kontext)


def forgot_password(request):
    kontext = {}
    return render(request, 'forgot-password.html', kontext)

def logout_view(request):
    form = FromLogin()
    logout(request)
    request.session.flush()
    return render(request, 'login.html',{'form':form})