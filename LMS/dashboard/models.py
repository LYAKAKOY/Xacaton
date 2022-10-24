from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name_course = models.CharField(verbose_name='Название курса', max_length=255)
    teacher = models.ManyToManyField(User, verbose_name='Преподавательcкий состав', related_name='Преподаватели')
    students = models.ManyToManyField(User, verbose_name='Студенты', related_name='Студенты')

    def __str__(self):
        return self.name_course

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lecture(models.Model):
    name_lecture = models.CharField(verbose_name='Название лекции', max_length=255)
    course = models.ForeignKey(Course, verbose_name='Название курса', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=False, auto_now_add=False, default=None)

    def __str__(self):
        return self.name_lecture

    class Meta:
        verbose_name = 'Лекция'
        verbose_name_plural = 'Лекции'
