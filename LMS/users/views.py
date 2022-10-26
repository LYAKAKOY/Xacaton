from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, \
    PasswordResetCompleteView
from django.shortcuts import resolve_url, redirect
from django.views.generic import CreateView
from rest_framework import generics, status
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .forms import RegisterForm, AuntificationUserForm, MyPasswordResetForm
from django.urls import reverse_lazy

# Create your views here.
from .serializers import UserRegisterSerializer


class RegisterUserApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)


class RegistrationUserView(CreateView):
    """Регистрация пользователя"""

    form_class = RegisterForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('dashboard')


class AuntificationUserView(LoginView):
    """Аутентификация пользователя"""

    form_class = AuntificationUserForm
    template_name = 'users/login.html'
    def get_success_url(self):
        return reverse_lazy('profile')

    def form_valid(self, form):
        remember_me = form.cleaned_data['remember_me']
        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True
        return super(AuntificationUserView, self).form_valid(form)

@login_required
def logout_user(request):
    logout(request)
    return redirect('log')


class ChangePasswordUser(PasswordResetView):
    """Изменение пароля пользователя"""

    template_name = 'users/password_reset.html'
    form_class = MyPasswordResetForm


class ChangePasswordUserConfirm(PasswordResetConfirmView):
    """Подтверждение изменения пароля"""

    template_name = 'users/password_reset_confirm.html'


class PasswordUserDone(PasswordResetDoneView):
    """Сообщение об отправке письма на почту"""

    template_name = 'users/password_reset_done.html'


class ChangePasswordUserComplete(PasswordResetCompleteView):
    """Сообщение о статусе изменение пароля"""

    template_name = 'users/password_reset_complete.html'
