from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm  
from django.contrib.auth import logout
from django.shortcuts import redirect

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def custom_logout_view(request):
    if request.user.is_staff:
        logout(request)
        return redirect('/admin/login/')
    else:
        logout(request)
        return redirect('/accounts/login/')