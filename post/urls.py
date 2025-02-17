from django.urls import path
from .views import post_list, post_create, post_update, post_delete, post_detail

urlpatterns = [
    path("", post_list, name="post_list"),
    path("create/", post_create, name="post_create"),
    path("<int:pk>/", post_detail, name="post_detail"),
    path("<int:pk>/update/", post_update, name="post_update"),
    path("<int:pk>/delete/", post_delete, name="post_delete"),
]
