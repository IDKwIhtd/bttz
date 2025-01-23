from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("user_profile")
    else:
        form = CustomUserCreationForm()
    return render(request, "signup.html", {"form": form})


@login_required
def user_logout(request):
    logout(request)
    return redirect("/post/")


@login_required
def user_profile(request):
    return render(request, "profile.html", {"user": request.user})
