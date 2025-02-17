# 데이터베이스 모델 (models)과 설정(settings)을 가져옴
from django.db import models
from django.conf import settings


# Create your models here.

# class TimestamedModel(
#     models.Model
# ):  # TimestampedModel은 다른 모델에서 상속할 추상 모델
#     created_at = models.DateTimeField(
#         auto_now_add=True
#     )  # 객체가 처음 생성될 때 자동으로 현재 시간이 저장됨
#     updated_at = models.DateTimeField(
#         auto_now=True
#     )  # 객체가 수정될 때 자동으로 현재 시간이 업데이트됨

#     class Meta:
#         abstract = True


# # Post 모델을 정의하며, TimeStampedModel을 상속하여 자동으로 created_at, updated_at을 가짐
# class Post(TimestampedModel):
#     author = models.ForeignKey(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE
#     )  # author: User 모델과 다대일 관계(ForeignKey) on_delete=models.CASCADE: 작성자가 삭제되면 해당 게시물도 삭제됨
#     message = models.TextField()  # message : 게시글 내용을 저장하는 TextField
#     tag_set = models.ManyToManyField(
#         "Tag", blank=True
#     )  # tag_set: 다대다 관계(ManyToManyField)를 사용해 Tag 모델과 연결, blank=True: 태그가 없어도 게시물 저장 가능

#     def __str__(self):
#         return self.message

# # Tag 모델을 정의하며, TimeStampedModel을 상속받음
# class Tag(TimestampedModel):
#     name = models.CharField(max_length=44) # name: 최대 44자의 문자열을 저장하는 필드

#     def __str__(self):
#         return self.name # Tag 모델의 문자열 표현을 name으로 설정


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
