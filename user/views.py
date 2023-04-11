from django.shortcuts import render, redirect
from .models import UserModel
from .forms import UserForm
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def signup(request):
    form = UserForm()
    if request.method == 'GET':
        return render(request, 'user/signup.html', { 'form' : form })
    elif request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password1')
            # user = authenticate(request, username=username, password=password)
            # login(request, user)
            return redirect('user/login')
        else:
            form = UserForm()
            return render(request, 'user/signup.html', {'form' : form})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        me = auth.authenticate(request, username=username, password=password)
        if me is not None:
            auth.login(request, me)
            return redirect('/')
        else:
            return render(request, 'user/login.html', {'error': '아이디 혹은 비밀번호를 확인 해 주세요'})

    elif request.method == 'GET':
        return render(request, 'user/login.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')
