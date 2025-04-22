from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)  # render : 템플릿을 렌더링하는 함수, redirect : 다른 URL로 리디렉션하는 함수
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Post
from .forms import PostForm
from .serializers import PostSerializer
from post.forms import PostForm  # PostForm : 게시물 폼을 가져옴
from post.models import Post  # Post : 게시물 모델을 가져옴
from rest_framework.permissions import IsAuthenticatedOrReadOnly


# ----------------------
# HTML 템플릿 기반 뷰
# ----------------------
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "post_detail_html.html", {"post": post})


def post_list(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "post_list_html.html", {"posts": posts})


# post_list : 모든 게시물을 가져와 템플릿 blog/post_list.html로 전달
# def post_list(request):
#     posts = Post.objects.all()
#     context = {"posts": posts}
#     return render(request=request, template_name="blog/post_list.html", context=context)


# ----------------------
# DRF API 기반 뷰
# ----------------------
class PostListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        posts = Post.objects.all().order_by("-created_at")
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        return get_object_or_404(Post, pk=pk)

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("post_list_html")
    else:
        form = PostForm()
    return render(request, "post_form.html", {"form": form})


def post_update(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("post_list_html")
    else:
        form = PostForm(instance=post)
    return render(request, "post_form.html", {"form": form})


def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("post_list_html")
    return render(request, "post_confirm_delete.html", {"post": post})
