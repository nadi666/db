from django.db import models
from django.db.models import Sum


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=50)
    work = models.CharField(max_length=50, choices=[('мастер', "мастер"), ("учитель", "учитель")], null=True)

    def __str__(self):
        return self.middle_name +' '+ self.name +' '+ self.last_name

class Speciality(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    course = models.CharField(max_length=50, choices=[("два года", "два года"),
                                                      ("три месяца", "три месяца"),
                                                      ("год (после 9)", "год (после 9)"),
                                                      ("год (после 9 и 11)", "год (после 9 и 11)")],
                              unique=True, null=True)
    education_form = models.CharField(max_length=50, choices=[('контракт', 'контракт'), ('бюджет', 'бюджет')])
    for_edu = models.CharField(max_length=10, choices=[('9', '9'), ('11', '11'), ('9 и 11', '9 и 11')], null=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=50, choices=[('man', 'мужчина'), ('woman', 'женщина')], default='')
    age = models.DateField('data')
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, null=True)
    course = models.CharField(max_length=50, choices=[('1', '1'), ('2', '2')], default='1', null=True)
    form_education = models.CharField(max_length=50, choices=[('контракт', 'контракт'), ('бюджет', 'бюджет')])

    def __str__(self):
        return f'{self.name, self.middle_name, self.last_name}'

class Subject(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teach', null=True)
    all_hour = models.IntegerField(null=False, default='')
    course_time = models.IntegerField(null=False, default='')
    cycle = models.CharField(max_length=255, choices=[('профессионально-техническое', 'профессионально-техническое'),
                                      ('общеобразовательное', 'общеобразовательное')], null=True)
    course = models.CharField(max_length=10, choices=[('1', '1'), ('2', '2')])
    specialization = models.ForeignKey(Speciality, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class Plan(models.Model):
    name = models.CharField(max_length=50, null=True)
    course = models.IntegerField(null=True)
    specialization = models.ForeignKey(Speciality, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class SubjectPlan(models.Model):
    number = models.PositiveIntegerField(default=0)

    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    cycle = models.CharField(max_length=50, choices=[('профессионально-техническое', 'профессионально-техническое'),
                                                     ('общеобразовательное', 'общеобразовательное')], null=True)
    total_hours = models.IntegerField(null=True)
    lpz_hours = models.IntegerField(default='0')
    self_study_hours = models.IntegerField(default='0')
    hours_per_course = models.IntegerField(null=True)

    def __str__(self):
        return self.specialization
