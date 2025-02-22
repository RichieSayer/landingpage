from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm, LoginForm
from django.contrib.auth import logout

# Create your views here.
def logout_view(request):
    logout(request)
    return redirect('home')

def home_view(request):
    return render(request, 'accounts/home.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})