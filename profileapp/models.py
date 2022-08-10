from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Profile(models.Model):
    # on_delete : 모델구현시 데이터베이스상에서 참조무결성을 유지하여 FK삭제시 해당 요소 처리방법
    # CASCADE : FK를 포함하는 모델 인스턴스도 같이 삭제,
    # PROTECT : 해당요소 같이 삭제 안시킴
    # SET_NULL : FK값을 널로 바꿈
    # SET_DEFAULT : default값으로 바꿈 (default가 있을때만 가능)

    # related_name : html에 쉽게 연결하기 위한 이름 설정 =>
    # OneToOneField를 통해 user객체와 profile 객채의 연결고리가 생성되어짐.!!!!!!!!
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    # 이미지저장
    # upload_to : 이미지를 서버 어디에 저장할지?
    image = models.ImageField(upload_to='profileapp/', null=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)
