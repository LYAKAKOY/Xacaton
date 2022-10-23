from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, \
    PasswordResetCompleteView
from django.views.generic import CreateView
from .forms import RegisterForm, AuntificationUserForm
from django.urls import reverse_lazy


# Create your views here.

class RegistrationUserView(CreateView):
    """Регистрация пользователя"""

    form_class = RegisterForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('')


class AuntificationUserView(LoginView):
    """Аутентификация пользователя"""

    form_class = AuntificationUserForm
    template_name = 'users/login.html'


class ChangePasswordUser(PasswordResetView):
    """Изменение пароля пользователя"""

    template_name = 'users/password_reset.html'


class ChangePasswordUserConfirm(PasswordResetConfirmView):
    """Подтверждение изменения пароля"""

    template_name = 'users/password_reset_confirm.html'


class PasswordUserDone(PasswordResetDoneView):
    """Сообщение об отправке письма на почту"""

    template_name = 'users/password_reset_done.html'


class ChangePasswordUserComplete(PasswordResetCompleteView):
    """Сообщение о статусе изменение пароля"""

    template_name = 'users/password_reset_complete.html'
