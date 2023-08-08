from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, redirect

from .models import Student, Teacher, Subject, Speciality, Plan, SubjectPlan
from .forms import StudentForm, TeacherForm, SubjectForm, SpecialityForm, PlanForm, SubjectPlanForm

def about_us(request):
    return render(request, 'about.html')

# ************** Student ******************
def student_list(request):
    students = Student.objects.all().order_by('middle_name')
    context = {'students': students}
    return render(request, 'student_db/student_list.html', context)

def student_create(request):
    if request.method == 'GET':
        if form.is_valid():
            form.save()
            return redirect('student:student_list')
    return render(request, 'student_db/student_form.html', {'form': form})



def student_filter(request):
    specialities = Speciality.objects.all()
    students = Student.objects.all()
    if request.method == 'POST':
        course = request.POST.get('course')
        speciality = request.POST.get('speciality')
        sex = request.POST.get('sex')
        form_education = request.POST.get('form_education')
        age = request.POST.get('age')
        if course:
            students = students.filter(course=course)
        if speciality:
            students = students.filter(speciality=speciality)
        if sex:
            students = students.filter(sex=sex)
        if form_education:
            students = students.filter(form_education=form_education)
        if age:
            students = students.filter(age__year=age)
    return render(request, 'student_db/student_filter.html', {'students': students, 'specialities': specialities})

# ************** Teacher *****************
def teacher_list(request):
    teachers = Teacher.objects.all().order_by('middle_name')
    context = {'teachers': teachers}
    return render(request, 'teacher/teacher_list.html', context)

def teacher_new(request):
    
def teacher_update(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    form = TeacherForm(request.POST or None, instance=teacher)
    context = {'form': form}
    if form.is_valid():
        form.save()
        return redirect('student:teacher_list')
    return render(request, 'teacher/teacher_form.html', context)

def teacher_delete(request, pk):
    return redirect('student:teacher_list')

