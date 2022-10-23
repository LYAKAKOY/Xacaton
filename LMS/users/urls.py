from django.urls import path
from .views import Registration

urlpatterns = [
    path('reg/', Registration.as_view(), name='reg')

]