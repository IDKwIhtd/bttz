# post/forms.py
from django import forms
from .models import Post
from post.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]


# # PostForm : ModelForm을 상속받아 자동으로 HTML 폼 생성
# class PostForm(forms.ModelForm):
#     class Meta:  # Meta :
#         model = Post  # Post 모델과 연결
#         fields = ["message", "tag_set"]  # message와 tag_set 필드만 폼에서 사용
