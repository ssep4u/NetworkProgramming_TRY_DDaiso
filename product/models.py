from django.core.validators import MinValueValidator
from django.db import models
from django.shortcuts import resolve_url


class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField(validators=[MinValueValidator(0)])  # PositiveIntegerField()
    image = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return f'{self.name}: {self.price}원'  # 이름: 가격원

    def get_absolute_url(self):  # 모델 하나를 구하는 절대 주소 구하자
        return resolve_url('product:detail', pk=self.id)


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.contents}'

    class Meta:
        ordering = ['-updated_at']
