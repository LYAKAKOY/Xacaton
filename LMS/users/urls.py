from django.urls import path
from .views import RegistrationUserView, AuntificationUserView, ChangePasswordUser

urlpatterns = [
    path('reg', RegistrationUserView.as_view(), name='reg'),
    path('login', AuntificationUserView.as_view(), name='log'),
    path('fogot_password', ChangePasswordUser.as_view(), name='pass_reset'),
    path()
]