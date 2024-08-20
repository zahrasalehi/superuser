from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm
import os


def register(request):
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
            return redirect('admin:index')
    else:
        form = UserRegistrationForm()
    return render(request, '/home/z4/Sources/dj-admin-signup/superuser/signup/templates/admin/registration/register.html', {'form': form})
