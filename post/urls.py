from django.urls import path
from .views import post_list, post_create, post_update, post_delete, post_detail
from post import views

urlpatterns = [
    path("", post_list, name="post_list"),  # 기본 경로(/)에서 post_list 뷰를 실행
    path("create/", post_create, name="post_create"),
    path("<int:pk>/", post_detail, name="post_detail"),
    path("<int:pk>/update/", post_update, name="post_update"),
    path("<int:pk>/delete/", post_delete, name="post_delete"),
    # path(route="", view=views.post_list, name="post_list"),
    path(
        route="post_new", view=views.post_new
    ),  # /post_new 경로에서 post_new 뷰를 실행
]
