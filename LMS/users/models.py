from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserData(models.Model):
    """Данные зарегистрированного пользователя"""

    firstname = models.CharField('Имя пользователя', max_length=255, default='')
    lastname = models.CharField('Фамилия пользователя', max_length=255, default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Данные пользователя'
        verbose_name_plural = 'Данные пользователей'
