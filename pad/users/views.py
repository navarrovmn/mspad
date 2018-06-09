from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth

from .forms import SignupForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username, password = data['username'], data['password']

            user = User.objects.create_user(
                username=username,
                password=password
            )

            user = auth.authenticate(
                request,
                username=username,
                password=password
            )

            auth.login(request, user)

            return redirect('/')
        return render(request, 'users/signup.html', {'form': form})
    else:
        return render(request, 'users/signup.html', {'form': SignupForm()})
