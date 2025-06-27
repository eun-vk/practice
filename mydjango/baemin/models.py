# baemin/models.py


from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

# 1 측
class Shop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # photo = models.FileField()  # 모든 파일 포맷 저장 가능
    photo = models.ImageField(upload_to='shop_photos/')  # 이미지만 받아요.
    class Shop(models.Model):
    # ...
        class Meta:
            ordering = ["-id"]

# N 측에 1에 대한 외래키 필드를 추가
class Review(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    content = models.TextField()
    # rating = models.IntegerField()  # 음수/양수 다 담을 수 있어요.
    # rating = models.PositiveIntegerField()   # 양수만 담을 수 있어요. 담을 수 있는 양수의 범위가 2배 커져요.
    rating = models.PositiveSmallIntegerField(
    # validators=[
    #     MinValueValidator(1), 
    #     MaxValueValidator(5)
    #     ],

    choices=[
            (1, '1점'),
            (2, '2점'),
            (3, '3점'),
            (4, '4점'),
            (5, '5점'),
        ],
        help_text="1점 ~ 5점 사이 점수를 주세요."
    )  #
    # Review쿼리셋에 대한 디폴트 정렬 
    # -Review 쿼리셋에서 order_by를 지정하지 않으면 자동으로 적용된다. 
    class Meta: 
        ordering = ["-id"]
    # 1 bit => 0 과 1을 표현 => 값을 2가지 표현 가능
    # 2 bit => 2 ** 2 => 총 4가지 표현 가능
    # 3 bit => 8가지
    # 4 bit => 16, 5 => 32, 6 => 64, 7 => 128, 8 => 256가지 숫자를 표현 가능.
    # 1 byte <= 8비트

    # 일반적인 숫자 변수는 4바이트(32비트)로 숫자를 표현. 물론 8바이트(64비트)로 표현도 해요.


