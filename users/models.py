from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """Информация о пользователе"""
    username = None

    email = models.EmailField(unique=True, verbose_name='email')
    phone = models.CharField(max_length=12, verbose_name='телефон')
    city = models.CharField(max_length=20, verbose_name = 'город')
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
