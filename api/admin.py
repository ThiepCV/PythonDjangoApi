from django.contrib import admin

# Register your models here.
from .models import Student, Teacher, Course, Candidate

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Candidate)