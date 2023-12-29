# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from .forms import LoginForm
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('dashboard_app:dashboard')
        else:
            messages.error(request, 'Invalid login. Please check your username and password! ')
    return render(request, 'login.html', {'form': LoginForm})

def logout(request):
    auth.logout(request)
    messages.info(request, 'You have been log out')
    return redirect('user_app:login')

