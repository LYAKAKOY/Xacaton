from django.db import models
from users.models import *


class Course(models.Model):
    name = models.CharField("Название курса", max_length=255, default='')
    users = models.ManyToManyField(UserData, related_name="courses")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lecture(models.Model):
    name = models.CharField("Название лекции", max_length=255, default='')
    date = models.DateTimeField("Дата")
    teacher = models.ForeignKey(UserData, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default='', related_name="lectures")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Лекция'
        verbose_name_plural = 'Лекции'