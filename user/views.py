from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth import login, logout, get_user_model
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

User = get_user_model()


class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializers = UserSerializer(users, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
    return redirect("/post/html/")


@login_required
def user_profile(request):
    return render(request, "profile.html", {"user": request.user})


class CustomLoginView(LoginView):
    def get_success_url(self):
        redirect_to = self.get_redirect_url()
        if not redirect_to or redirect_to == self.request.path:
            return resolve_url("/post/html/")
        return redirect_to
