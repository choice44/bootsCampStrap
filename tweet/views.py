from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import UserModel, TweetModel, CommentModel
from .forms import TweetForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def home(request):
    return redirect('tweet/')


@login_required
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


def show_tweet(request):
    all_tweet = TweetModel.objects.all().order_by('-created_at')
    return render(request, 'tweet/home.html', {'all_tweet': all_tweet})


def detail_tweet(request, detail_id):
    if request.method == 'GET':
        detail_tweet = TweetModel.objects.filter(id=detail_id).first()
        tweet_comment = CommentModel.objects.filter(
            tweet_id=detail_id).order_by('-created_at')
        return render(request, 'tweet/detail_tweet.html', {'detail': detail_tweet, 'comment': tweet_comment})


@login_required
def update_tweet(request, update_id):
    update = TweetModel.objects.filter(id=update_id).first()
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


@login_required
def write_comment(request, detail_id):
    if request.method == 'POST':
        comment = request.POST.get("comment", "")
        current_tweet = TweetModel.objects.get(id=detail_id)

        TC = CommentModel()
        TC.comment = comment
        TC.author = request.user
        TC.tweet = current_tweet
        TC.save()

        return HttpResponseRedirect(reverse(detail_tweet, args=[detail_id]))

# deletecomment - 댓글 삭제하기


@login_required
def delete_comment(request, detail_id):
    comment = CommentModel.objects.get(id=detail_id)
    current_tweet = comment.tweet.id
    comment.delete()
    return redirect('/tweet/detail/' + str(current_tweet))


# updatecomment - 댓글 수정하기
def update_comment(request, detail_id):
    comment = CommentModel.objects.get(id=detail_id)
    current_tweet = comment.tweet.id
    comment.update()
    return redirect('/tweet/detail' + str(current_tweet))


# commentshow 함수를 따로 작성할지
# show_tweet 함수에 넣을지는 고민해봐야 할듯


# 태그는 고민해보겠음-시간없으면 안만들거임
# tagcloud
