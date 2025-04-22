from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import signup, user_profile, user_logout, CustomLoginView

urlpatterns = [
    path("", user_profile, name="user_home"),
    path("signup/", signup, name="signup"),
    path("login/", CustomLoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", user_logout, name="logout"),
    path("profile/", user_profile, name="user_profile"),
]
