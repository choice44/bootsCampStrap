from django.shortcuts import render, redirect
from .models import UserModel
from .forms import UserForm, EditProfileForm, FileForm
from tweet.views import my_page
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse


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


@login_required
def edit_profile_view(request, pk):
    user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            my_page_url = reverse(
                'my_page', kwargs={'user_id': request.user.pk})
            return redirect(my_page_url)
    else:
        form = EditProfileForm(instance=user)

    return render(request, 'user/edit_profile.html', {'form': form})


def follow_function(request, user_id):
    login_user = UserModel.objects.get(id=request.user.id)
    follow_user = UserModel.objects.get(id=user_id)
    follow_user_all = follow_user.follow.all()

    if login_user.id != user_id:
        if login_user in follow_user_all:
            follow_user.follow.remove(login_user.id)
            follow_user.save()
        else:
            follow_user.follow.add(login_user.id)
            follow_user.save()

    return HttpResponseRedirect(reverse(my_page, args=[user_id]))


def uploadtest_view(request):
    if request.method == 'GET':
        form = FileForm()
        return render(request, 'user/test.html', {'form': form})
    elif request.method == "POST":
        # file = request.FILES.get('imgfile')
        # fileupload = FileForm(file)
        # fileupload.save()
        # return redirect('/user/uploadtest')
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            print("여기")
            form.save()
            return redirect('/user/uploadtest')
        else:
            print("저기")
            form = FileForm()
            return render(request, 'user/test.html', {'form': form})
