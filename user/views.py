from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages


def authentication(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'auth.html')


def login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'Either username or password is incorrect')

    return redirect('auth')


def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            user = User.objects.create_user(username=username, password=password1)

            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Password does not match")
    return redirect('auth')
