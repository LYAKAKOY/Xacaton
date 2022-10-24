from django.shortcuts import render
from django.views.generic import View
from .models import UserData
import datetime
from dashborad.days import get_days_in_month

class CoursesView(View):

    def get(self, request):
        current_user_d = UserData.objects.get(user=request.user.id)
        courses = current_user_d.courses.all()
        days = [i for i in range(1, get_days_in_month()+1)]

        return render(request, 'dashboard.html', {"courses": courses, "days": days})
