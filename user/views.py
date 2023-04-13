from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from tweet.views import my_page
from tweet.models import TweetModel
from .models import UserModel
from .forms import UserForm, EditProfileForm, FileForm


def signup_view(request):
    form = UserForm()
    if request.method == 'GET':
        return render(request, 'user/signup.html', {'form': form})
    elif request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():  # 폼 유효성검사
            form.save()
            # 유효성 검사를 통과한 데이터(cleaned_data)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            form = UserForm()
            return render(request, 'user/signup.html', {'form': form, 'error': "회원가입 실패!"})


# 로그인_리콰이얼드 데코레이션으로 로그인되어 있지 않은 자가 이 함수를 호출했을 때 login_url로 지정한 경로로 이동된다.
@login_required(login_url='/user/login')
def edit_profile_view(request, pk):  # 매개변수 pk 무조건 받아와야 작동
    user = request.user
    if request.method == 'POST':
        # 인스턴스 안적으면 새로운 객체가 생성됨됨이
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
        else:
            follow_user.follow.add(login_user.id)

    return HttpResponseRedirect(reverse(my_page, args=[user_id]))


@login_required(login_url='/user/login')
def follow_tweet_view(request):
    login_user = request.user
    follow_users = login_user.follower.all()
    follow_users_ids = [user.id for user in follow_users]
    follow_tweet = TweetModel.objects.filter(
        user_id__in=follow_users_ids)  # __in : 장고 ORM에서 사용되는 연산자, 객체의 속성에 접근하고 조건을 지정
    all_follow_tweet = follow_tweet.order_by('-created_at')
    return render(request, 'tweet/follows_tweet.html', {'all_follow_tweet': all_follow_tweet})


def user_image_upload(request, user_id):
    if request.method == 'GET':
        form = FileForm()
        return render(request, 'user/user_image_upload.html', {'form': form})
    elif request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            user = UserModel.objects.get(id=request.user.id)
            user.imgfile = form.cleaned_data.get('imgfile')
            user.save()
            return redirect('/tweet/mypage/'+str(user_id))
        else:
            form = FileForm()
            return render(request, 'user/user_image_upload.html', {'form': form})
