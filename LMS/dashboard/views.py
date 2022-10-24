from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import View
from .models import UserData
import datetime


class CoursesView(View):

    def get(self, request):
        current_user_d = UserData.objects.get(user=request.user.id)
        courses = current_user_d.courses.all()

        return render(request, 'dashboard.html', {"courses": courses})
