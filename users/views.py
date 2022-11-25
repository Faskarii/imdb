from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import User
from .forms import UserSignUpForm, UserChangPasswordForm, UserResetPasswordForm, UserProfileForm
from django.contrib import messages


def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'auth_error': False})

    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        print(email, password)
        user = authenticate(request, username=email, password=password)
        print(user)
        if user:
            login(request, user)
            messages.SUCCESS(request, f'Welcome {user}')
            return redirect('/')

        else:
            messages.ERROR(request, f'Authentication fail')
            return render(request, 'login.html', {'auth_error': True})


def user_sign_up(request):
    if request.method == 'GET':
        form = UserSignUpForm()
        context = {'form': form}
        return render(request, 'signup.html', context)
    elif request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'signup.html', {'form': form})


def user_view(request, pk):
    if request.method == 'GET':
        user = request.user
        form = UserProfileForm(instance=user)
        return render(request, 'profile.html')