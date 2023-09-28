from django.db import models
from django.contrib.auth.models import User, AbstractUser

class Product(models.Model):
    """Продукт - может содержать множество уроков"""
    title = models.CharField(max_length=225)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    """Урок - может находиться в множестве продуктов"""
    products = models.ManyToManyField(Product)
    title = models.CharField(max_length=255)
    video_url = models.URLField(max_length=255)
    video_duration = models.DurationField()

    def __str__(self):
        return self.title

class Product_Permission(models.Model):
    """Доступ - содержит пользователя и доступные ему продукты"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)

# Create your models here.
