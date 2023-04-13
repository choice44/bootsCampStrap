from django.shortcuts import render, redirect
from .models import UserModel
from .forms import UserForm, EditProfileForm
from tweet.views import my_page
from tweet.models import TweetModel
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


@login_required
def follow_tweet_view(request):
    login_user = request.user
    follow_users = login_user.follower.all()
    follow_users_ids = [user.id for user in follow_users]
    follow_tweet = TweetModel.objects.filter(user_id__in=follow_users_ids)
    all_follow_tweet = follow_tweet.order_by('-created_at')
    return render(request, 'tweet/follows_tweet.html', {'all_follow_tweet': all_follow_tweet})
