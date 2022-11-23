from django.shortcuts import render
from django.contrib.auth import login, authenticate
from .models import User


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

