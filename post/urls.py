from django.urls import path
from .views import (
    post_list,
    post_create,
    post_update,
    post_delete,
    post_detail,
    post_like_html,
    comment_create,
    comment_delete,
    comment_update,
    PostListView,
    PostDetailView,
    PostLikeAPIView,
    CommentListCreateAPIView,
)
from post import views

urlpatterns = [
    # 템플릿 기반 HTML 뷰
    path("html/", post_list, name="post_list_html"),
    path("html/<int:pk>/", post_detail, name="post_detail_html"),
    path("html/create/", post_create, name="post_create_html"),
    path("html/<int:pk>/update/", post_update, name="post_update_html"),
    path("html/<int:pk>/delete/", post_delete, name="post_delete_html"),
    path("html/<int:pk>/like/", post_like_html, name="post_like_html"),
    path("html/<int:pk>/comment/", comment_create, name="comment_create_html"),
    path(
        "html/comment/<int:comment_pk>/delete/",
        comment_delete,
        name="comment_delete_html",
    ),
    path(
        "html/comment/<int:comment_pk>/update/",
        comment_update,
        name="comment_update_html",
    ),
    # API 뷰
    path("", PostListView.as_view(), name="post_list_api"),
    path("<int:pk>/", PostDetailView.as_view(), name="post_detail_api"),
    path("<int:pk>/like/", PostLikeAPIView.as_view(), name="post_like_api"),
    path(
        "<int:pk>/comments/",
        CommentListCreateAPIView.as_view(),
        name="commnet_list_create_api",
    ),
]
