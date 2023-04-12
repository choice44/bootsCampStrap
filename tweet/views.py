from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .models import UserModel, TweetModel
from .forms import TweetForm


def home(request):
    return redirect('tweet/')


@login_required
def create_tweet(request):
    if request.method == 'GET':
        tweet_create = TweetForm()
        return render(request, 'tweet/create.html', {'create_tweet_form': tweet_create})
    
    elif request.method == 'POST':
        user = request.user
        tweet_form = TweetForm(request.POST)
        tweet_form_post = tweet_form.save(commit=False)
        tweet_form_post.user = user
        tweet_form_post.save()
        return redirect('/')


def show_tweet(request):
    all_tweet = TweetModel.objects.all().order_by('-created_at')
    return render(request, 'tweet/home.html', {'all_tweet': all_tweet})


def detail_tweet(request, detail_id):
    if request.method == 'GET':
        detail_tweet = TweetModel.objects.filter(id=detail_id).first()
        return render(request, 'tweet/detail_tweet.html', {'detail': detail_tweet})


@login_required
def update_tweet(request, update_id):
    update = TweetModel.objects.filter(id=update_id).first()
    if request.method == 'GET':
        update_form = TweetForm(instance=update)
        return render(request, 'tweet/edit_tweet.html', {'update_form': update_form, 'update_id': update_id})

    elif request.method == 'POST':
        update_content = TweetForm(request.POST, instance=update)
        update_post_content = update_content.save(commit=False)
        update_post_content.save()
        return redirect('/tweet')


@login_required
def delete_tweet(request, delete_id):
    tweet = TweetModel.objects.get(id=delete_id)
    tweet.delete()
    return redirect('/tweet')


@login_required
def my_page(request, user_id):
    user = UserModel.objects.get(id=user_id)
    my_page = user.tweet.all()
    return render(request, 'tweet/my_page.html', {'my_tweet': my_page})


@login_required
def like_create(request, tweet_id):
    tweet = TweetModel.objects.get(id=tweet_id)
    user = request.user
    if tweet.like.all():
        tweet.like.remove(user)
    else:
        tweet.like.add(user)
    return redirect('/tweet')
