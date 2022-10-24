from django.urls import path, include
from .views import CoursesView

urlpatterns = [
    path('dashboard/', CoursesView.as_view(), name='courses')
]