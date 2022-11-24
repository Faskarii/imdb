from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from .models import User


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
            print()
            return HttpResponseRedirect('/')

        else:
            return render(request, 'login.html', {'auth_error': True})
