from django.conf import settings  # Django의 기본설정(settings)
from django.contrib.auth.models import AbstractUser  # 기본 사용자 모델 (AbstractUser)
from django.db import models  # 데이터베이스 모델(models)


# Create your models here.


# User 모델을 Django의 기본 사용자 모델(AbstractUser)을 상속받아 확장
# class User(AbstractUser):
#     bio = models.TextField()  # bio 필드 추가 (사용자의 자기소개를 저장하는 TextField)


# Profile 모델을 정의
class Profile(models.Model):
    user = models.OneToOneField(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )  # user: OneToOneField를 사용해 User 모델과 1:1 관계 설정, on_delete=models.CASCADE: User가 삭제되면 Profile도 삭제됨
    address = models.CharField(
        max_length=50
    )  # address: 최대 50자의 문자열을 저장하는 필드
    zipcode = models.CharField(
        max_length=6
    )  # zipcode: 최대 6자의 문자열을 저장하는 필드

    def __str__(self):
        return self.address  # Profile 모델의 문자열 표현을 주소(address)로 설정


class CustomUser(AbstractUser):
    profile_image = models.ImageField(
        upload_to="profile_images/", blank=True, null=True
    )
    bio = models.TextField(blank=True, null=True)
