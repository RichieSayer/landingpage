from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, LoginForm, UserEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages

# Get the custom user model
CustomUser = get_user_model()

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
    next_url = request.GET.get('next', 'home')  # Default to 'home' if no next URL is provided

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # If the user is staff and no 'next' URL is specified, send them to the admin dashboard
            if user.is_staff and next_url == 'home':
                return redirect('admin_dashboard')

            return redirect(next_url)
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})

@login_required
def admin_dashboard_view(request):
    if not request.user.is_staff:
        return redirect('home')  # Or a permission denied page

    user_count = CustomUser.objects.count()  # Use the correct user model
    context = {'user_count': user_count}
    return render(request, 'accounts/admin_dashboard.html', context)

@login_required
def admin_user_list(request):
    if not request.user.is_staff:
        return redirect('home')

    users = CustomUser.objects.all()  # Use the correct user model
    return render(request, 'accounts/admin_user_list.html', {'users': users})

@login_required
def admin_user_edit(request, pk):
    if not request.user.is_staff:
        return redirect('home')

    user = get_object_or_404(CustomUser, pk=pk)  # Use the correct user model

    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            result = form.save()  # Save the form and handle deletion
            if result is None:  # User was deleted
                messages.success(request, 'User deleted successfully.')
                return redirect('admin_user_list')  # Redirect to user list after deletion
            else:
                messages.success(request, 'User updated successfully.')
                return redirect('admin_user_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserEditForm(instance=user)

    return render(request, 'accounts/admin_user_edit.html', {'form': form, 'user': user})
