from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from django.shortcuts import render, redirect, resolve_url, get_object_or_404
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


class UserDetailView(APIView):
    def get_object(self, pk):
        return get_object_or_404(User, pk=pk)

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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
