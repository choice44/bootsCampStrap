from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse
from .models import UserModel, TweetModel, CommentModel
from .forms import TweetForm, CommentForm
import os


def home(request):
    return redirect('tweet/')


def show_tweet(request):
    all_tweet = TweetModel.objects.all().order_by('-created_at')
    return render(request, 'tweet/home.html', {'all_tweet': all_tweet})


@login_required(login_url='/user/login')
def create_tweet(request):
    if request.method == 'GET':
        tweet_create = TweetForm()
        return render(request, 'tweet/create.html', {'create_tweet_form': tweet_create})

    elif request.method == 'POST':
        tw_f = TweetForm(request.POST, request.FILES)
        # form에서 유저를 받지 않으므로 임시저장된 form파일에 로그인 유저를 삽입
        if tw_f.is_valid():
            tw_f.image = tw_f.cleaned_data.get('image')
            tw_form = tw_f.save(commit=False)
            tw_form.user = request.user
            tw_f.save()
            return redirect('/')
        else:
            tweet_create = TweetForm()
            return render(request, 'tweet/create.html', {'create_tweet_form': tweet_create})


def detail_tweet(request, detail_id):
    detail_tweet = TweetModel.objects.filter(id=detail_id).first()
    tweet_comment = CommentModel.objects.filter(
        tweet_id=detail_id).order_by('-created_at')
    return render(request, 'tweet/detail_tweet.html', {'detail': detail_tweet, 'comment': tweet_comment})


@login_required(login_url='/user/login')
def update_tweet(request, update_id):
    tweet = TweetModel.objects.get(id=update_id)
    update = TweetModel.objects.filter(id=update_id).first()
    if request.user == tweet.user:
        if request.method == 'GET':
            update_form = TweetForm(instance=update)
            return render(request, 'tweet/edit_tweet.html', {'update_form': update_form, 'update_id': update_id})

        elif request.method == 'POST':
            update_content = TweetForm(
                request.POST, request.FILES, instance=update)

            if update_content.is_valid():
                update_post_content = update_content.save(commit=False)
                update_post_content.image = update_content.cleaned_data.get(
                    'image')
                if not update_content.cleaned_data.get(
                        'image'):
                    os.remove(os.path.join(
                        settings.MEDIA_ROOT, tweet.image.path))
                    update_post_content.image = ''
                update_post_content.save()
                return redirect('/tweet/')
            else:
                update_form = TweetForm(instance=update)
                return render(request, 'tweet/edit_tweet.html', {'update_form': update_form, 'update_id': update_id})
    else:
        return redirect('/')


@login_required(login_url='/user/login')
def delete_tweet(request, delete_id):
    user = request.user
    tweet = TweetModel.objects.get(id=delete_id)
    if user == tweet.user:
        tweet.delete()
        return redirect('/tweet/')
    else:
        return redirect('/')


def my_page(request, user_id):
    user = UserModel.objects.get(id=user_id)
    my_page = user.tweet.all().order_by('-created_at')
    return render(request, 'tweet/my_page.html', {'my_tweet': my_page, 'my_page_user': user})


@login_required(login_url='/user/login')
def like_create(request, tweet_id):
    tweet = TweetModel.objects.get(id=tweet_id)
    user = request.user
    if user in tweet.like.all():
        tweet.like.remove(user)
        return JsonResponse({'message': 'deleted', 'like_cnt': tweet.like.count()})
    else:
        tweet.like.add(user)
        return JsonResponse({'message': 'added', 'like_cnt': tweet.like.count()})


# 댓글 기능 view
# writecomment - 댓글 작성하기
@login_required(login_url='/user/login')
def write_comment(request, detail_id):
    if request.method == 'POST':
        comment = request.POST.get("comment", "")
        current_tweet = TweetModel.objects.get(id=detail_id)

        TC = CommentModel()
        TC.comment = comment
        TC.author = request.user
        TC.tweet = current_tweet
        TC.save()

        return redirect('/tweet/detail/' + str(detail_id))


# deletecomment - 댓글 삭제하기
@login_required(login_url='/user/login')
def delete_comment(request, comment_id):
    comment = CommentModel.objects.get(id=comment_id)
    current_tweet = comment.tweet.id
    if request.user == comment.author:
        comment.delete()
        return redirect('/tweet/detail/' + str(current_tweet))
    else:
        return redirect('/tweet/')


# updatecomment - 댓글 수정하기
@login_required(login_url='/user/login')
def update_comment(request, comment_id):
    update = CommentModel.objects.filter(id=comment_id).first()
    current_tweet = update.tweet.id
    if request.method == 'GET':
        update_form = CommentForm(instance=update)
        return render(request, 'tweet/detail_tweet.html', {'update_form': update_form, 'comment_id': comment_id})
    elif request.method == 'POST':
        update_comment = CommentForm(request.POST, instance=update)
        update_comment_save = update_comment.save(commit=False)
        update_comment_save.save()
        return redirect('/tweet/detail/' + str(current_tweet))
