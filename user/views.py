from django.shortcuts import render, redirect
from .models import UserModel
from .forms import UserForm
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def signup_view(request):
    form = UserForm()
    if request.method == 'GET':
        return render(request, 'user/signup.html', {'form': form})
    elif request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            form = UserForm()
            return render(request, 'user/signup.html', {'form': form})
