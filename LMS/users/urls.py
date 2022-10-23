from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.urls import path
from .views import RegistrationUserView, AuntificationUserView, ChangePasswordUser, PasswordUserDone, \
    ChangePasswordUserConfirm, ChangePasswordUserComplete

urlpatterns = [
    path('reg/', RegistrationUserView.as_view(), name='reg'),
    path('login/', AuntificationUserView.as_view(), name='log'),
    path('pass-reset/', ChangePasswordUser.as_view(), name='pass-reset'),
    path('password_reset_confirm/<uidb64>/<token>/', ChangePasswordUserConfirm.as_view(),
         name='password_reset_confirm'),
    path('password_reset_done/', PasswordUserDone.as_view(), name='password_reset_done'),
    path('password_reset_complete/', ChangePasswordUserComplete.as_view(), name='password_reset_complete')

]