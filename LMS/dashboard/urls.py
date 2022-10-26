from django.urls import path, include
from .views import CoursesView, CourseView, LectureView, lectures_day, profile, AllCoursesView

urlpatterns = [
    path('dashboard/', CoursesView.as_view(), name='dashboard'),
    path('dashboard/profile/', profile, name='profile'),
    path('dashboard/course/<slug:slug_course>/', CourseView.as_view(), name='course'),
    path('dashboard/course/lecture/<slug:slug_lecture>/', LectureView.as_view(), name='lecture'),
    path('dashboard/course/lectures/<int:day_lecture>/', lectures_day, name='l_day'),
    path('dashboard/allcourses/', AllCoursesView.as_view(), name='all_courses'),

]