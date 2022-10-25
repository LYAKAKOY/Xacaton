from django.urls import path, include
from .views import CoursesView, CourseView, LectureView

urlpatterns = [
    path('dashboard/', CoursesView.as_view(), name='courses'),
    path('dashboard/course/<slug:slug_course>/', CourseView.as_view(), name='course'),
    path('dashboard/course/lecture/<slug:slug_lecture>/', LectureView.as_view(), name='lecture')
]