from django.urls import path
from .views import Register

urlpatterns = [
    path('reg/', Register.as_view(), name='reg')

]