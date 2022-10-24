from django.urls import path
from dashborad.views import CoursesView

urlpatterns = [
    path('dashboard/', CoursesView.as_view(), name='dashboard')
]
