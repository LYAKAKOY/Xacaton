from django.contrib import admin
from .models import Course, Lecture


class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name_course",)}


class LectureAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name_lecture",)}


admin.site.register(Course, CourseAdmin)
admin.site.register(Lecture, LectureAdmin)
