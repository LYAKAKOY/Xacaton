from django.urls import path, include
from .views import RegistrationUserView, AuntificationUserView, ChangePasswordUser, PasswordUserDone, \
    ChangePasswordUserConfirm, ChangePasswordUserComplete, RegisterUserApiView

urlpatterns = [
    path('reg/', RegistrationUserView.as_view(), name='reg'),
    path('login/', AuntificationUserView.as_view(), name='log'),
    path('pass-reset/', ChangePasswordUser.as_view(), name='pass-reset'),
    path('password_reset_confirm/<uidb64>/<token>/', ChangePasswordUserConfirm.as_view(),
         name='password_reset_confirm'),
    path('password_reset_done/', PasswordUserDone.as_view(), name='password_reset_done'),
    path('password_reset_complete/', ChangePasswordUserComplete.as_view(), name='password_reset_complete'),
    path('api/v1/reg_user/', RegisterUserApiView.as_view(), name='reg_user_api'),
    path('api/v1/drf-auth/', include('rest_framework.urls'))

]