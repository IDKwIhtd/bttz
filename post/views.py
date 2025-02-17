from django.shortcuts import (
    render,
    redirect,
)  # render : 템플릿을 렌더링하는 함수, redirect : 다른 URL로 리디렉션하는 함수
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Post
from .forms import PostForm
from post.forms import PostForm  # PostForm : 게시물 폼을 가져옴
from post.models import Post  # Post : 게시물 모델을 가져옴


# Create your views here.
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "post_detail.html", {"post": post})


def post_list(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "post_list.html", {"posts": posts})


# post_list : 모든 게시물을 가져와 템플릿 blog/post_list.html로 전달
# def post_list(request):
#     posts = Post.objects.all()
#     context = {"posts": posts}
#     return render(request=request, template_name="blog/post_list.html", context=context)


# post_new : 새로운 게시물을 생성하는 뷰
def post_new(request):
    if request.method == "POST":  # POST 요청이 들어오면,
        form = PostForm(request.POST)  # PostForm을 사용해 유효성 검사 후 저장
        if form.is_valid():
            print(request.user)
            post = form.save(commit=False)
            post.author = (
                request.user
            )  # 저장할 때 author를 현재 로그인한 사용자로 설정 후 저장
            post.save()
            return redirect("post_list")  # 저장이 완료되면 post_list로 리디렉트
    else:  # GET 요청이 들어오면
        form = PostForm()  # 빈 폼을 생성하여
    return render(
        request, template_name="post/post_new.html", context={"form": form}
    )  # post/post_new.html로 렌더링


@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("post_list")
    else:
        form = PostForm()
    return render(request, "post_form.html", {"form": form})


def post_update(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("post_list")
    else:
        form = PostForm(instance=post)
    return render(request, "post_form.html", {"form": form})


def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("post_list")
    return render(request, "post_confirm_delete.html", {"post": post})
