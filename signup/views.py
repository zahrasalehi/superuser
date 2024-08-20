from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm, AdminAuthenticationForm
import os
from django.utils.translation import gettext_lazy as _


def register(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            # Automatically log in the user after registration
            user = authenticate(username=user.username, password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
            return redirect('/index/')
    return render(request, './register.html', {'form': form})


def custom_login_view(request):
    form = AdminAuthenticationForm()

    if request.method == "POST":
        form = AdminAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/index/')  # Redirect to the admin index page
    return render(request, 'login.html', {'form': form})
