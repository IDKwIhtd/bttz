from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Post
from .forms import PostForm


# Create your views here.
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "post_detail.html", {"post": post})


def post_list(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "post_list.html", {"posts": posts})


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
