from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserData(models.Model):
    """Данные зарегистрированного пользователя"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='pictures', default='pictures/mirea_maskot.png')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Данные пользователя'
        verbose_name_plural = 'Данные пользователей'
