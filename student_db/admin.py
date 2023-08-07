from django.contrib import admin
from .models import Student, Teacher, Subject, Speciality, Plan, SubjectPlan

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Speciality)
admin.site.register(Plan)
admin.site.register(SubjectPlan)