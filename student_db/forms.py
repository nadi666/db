from django import forms
from django.conf import settings

from .models import Student, Teacher, Subject, Speciality, Plan, SubjectPlan


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        data = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
        widgets = {'age': forms.TextInput(attrs={'placeholder': '%Y-%m-%d'})}

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

class SpecialityForm(forms.ModelForm):
    class Meta:
        model = Speciality
        fields = '__all__'

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'

class SpecialityForm(forms.ModelForm):
    class Meta:
        model = Speciality
        fields = '__all__'

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = '__all__'

class SubjectPlanForm(forms.ModelForm):
    class Meta:
        model = SubjectPlan
        fields = '__all__'