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
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student:student_list')
    else:
        form = StudentForm()
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
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student:teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'teacher/teacher_form.html', {'form': form})

def teacher_update(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    form = TeacherForm(request.POST or None, instance=teacher)
    context = {'form': form}
    if form.is_valid():
        form.save()
        return redirect('student:teacher_list')
    return render(request, 'teacher/teacher_form.html', context)

def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    teacher.delete()
    return redirect('student:teacher_list')

def teacher_filter(request):
    teachers = Teacher.objects.all()
    subject = request.GET.get('subject')
    if subject:
        teachers = teachers.filter(subject=subject)
    name = request.GET.get('name')
    if name:
        teachers = teachers.filter(name=name)
    middle_name = request.GET.get('middle_name')
    if middle_name:
        teachers = teachers.filter(middle_name=middle_name)
    last_name = request.GET.get('last_name')
    if last_name:
        teachers = teachers.filter(last_name=last_name)
    work = request.GET.get('work')
    if work:
        teachers = teachers.filter(work=work)
    context = {'teachers': teachers}
    return render(request, 'teacher/teacher_filter.html', context)


# ************** Speciality ******************
def speciality_list(request):
    specialities = Speciality.objects.all()
    context = {'specialities': specialities}
    return render(request, 'speciality/speciality_list.html', context)

def create_speciality(request):
    if request.method == 'POST':
        form = SpecialityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student:speciality_list')
    else:
        form = SpecialityForm()
    return render(request, 'speciality/speciality_form.html', {'form': form})

def speciality_delete(request, pk):
    speciality = get_object_or_404(Speciality, pk=pk)
    speciality.delete()
    return redirect('student:speciality_list')

def speciality_update(request, pk):
    speciality = get_object_or_404(Speciality, pk=pk)
    form = SpecialityForm(request.POST, instance=speciality)
    context = {'form': form}
    if form.is_valid():
        form.save()
        return redirect('student:speciality_list')
    return render(request, 'speciality/speciality_form.html', context)

def speciality_filter(request):
    specialities = Speciality.objects.all()
    teachers = Teacher.objects.all()
    if request.method == 'POST':
        name=request.POST.get('name')
        education_form=request.POST.get('education_form')
        course=request.POST.get('course')
        teacher=request.POST.get('teacher')
        if name:
            specialities=specialities.filter(name=name)
        if education_form:
            specialities=specialities.filter(education_form=education_form)
        if course:
            specialities=specialities.filter(course=course)
        if teacher:
            specialities=specialities.filter(teacher=teacher)
    return render(request, 'speciality/speciality_filter.html', {'specialities': specialities, 'teachers': teachers})

# ************** Subject ******************
def subject_list(request):
    specializations = Speciality.objects.all()
    technical_subject = Subject.objects.filter(cycle='профессионально-техническое').order_by('name')
    general_subject = Subject.objects.filter(cycle='общеобразовательное').order_by('name')
    context = {'specializations': specializations,
               'technical_subject': technical_subject,
               'general_subject': general_subject}
    return render(request, 'subject/subject_list.html', context)

def subject_all(request):
    technical_subject = Subject.objects.filter(cycle='профессионально-техническое').order_by('name')
    general_subject = Subject.objects.filter(cycle='общеобразовательное').order_by('name')
    context = {
               'technical_subject': technical_subject,
               'general_subject': general_subject}
    return render(request, 'subject/subject_all.html', context)

def subject_create(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student:subject_list')
    else:
        form = SubjectForm()
    context = {'form': form}
    return render(request, 'subject/subject_form.html', context)

def delete_subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    subject.delete()
    return redirect('student:subject_list')

def subject_update(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    form = SubjectForm(request.POST, instance=subject)
    context = {'form': form}
    if form.is_valid():
        form.save()
        return redirect('student:subject_list')
    return render(request, 'subject/subject_form.html', context)

def subject_filter(request):
    subjects = Subject.objects.all()
    teachers = Teacher.objects.all()
    specialities = Speciality.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        course = request.POST.get('course')
        teacher = request.POST.get('teacher')
        speciality = request.POST.get('speciality')
        if name:
            subjects = subjects.filter(name=name)
        if course:
            subjects = subjects.filter(course=course)
        if teacher:
            subjects = subjects.filter(teacher=teacher)
        if speciality:
            subjects = subjects.filter(speciality=speciality)
    return render(request, 'subject/subject_filter.html', {'subjects': subjects, 'teachers': teachers, 'specialities': specialities})

# ********** Study plan ******************
def all_plans(request):
    plans = Plan.objects.all().order_by('name')
    return render(request, 'studyplan/plan.html', {'plans': plans})

def calculate_total_hours(subject_plans, cycle):
    return subject_plans.filter(cycle=cycle).aggregate(Sum('total_hours'))['total_hours__sum']

def calculate_total_hours(subject_plans, cycle):
    return subject_plans.filter(cycle=cycle).aggregate(Sum('total_hours'))['total_hours__sum']

def view_plan(request, pk):
    plan = get_object_or_404(Plan, pk=pk)
    subject_plans = SubjectPlan.objects.filter(plan=plan)

    total_professional_hours = calculate_total_hours(subject_plans, 'профессионально-техническое')
    total_general_hours = calculate_total_hours(subject_plans, 'общеобразовательное')

    total_lpz_hours = subject_plans.aggregate(Sum('lpz_hours'))['lpz_hours__sum']
    total_hours_per_course = subject_plans.aggregate(Sum('hours_per_course'))['hours_per_course__sum']
    total_self_study_hours = subject_plans.aggregate(Sum('self_study_hours'))['self_study_hours__sum']

    return render(request, 'studyplan/study_plan_detail.html', {
        'plan': plan,
        'subject_plans': subject_plans,
        'total_professional_hours': total_professional_hours,
        'total_general_hours': total_general_hours,
        'total_lpz_hours': total_lpz_hours,
        'total_hours_per_course': total_hours_per_course,
        'total_self_study_hours': total_self_study_hours,
    })

def create_plan(request):
    if request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student:all_plans')
    else:
        form = PlanForm()
    return render(request, 'studyplan/plan_create.html', {'form': form})

def edit_plan(request, pk):
    plan = get_object_or_404(Plan, pk=pk)
    form = PlanForm(request.POST or None, instance=plan)
    context = {'form': form}
    if form.is_valid():
        form.save()
        return redirect('student:all_plans')
    return render(request, 'studyplan/studyplan_edit.html', context)

def delete_plan(request, pk):
    plan = get_object_or_404(Plan, pk=pk)
    plan.delete()
    return redirect('student:all_plans')

def delete_all_plans(request):
    if request.method == 'POST':
        Plan.objects.all().delete()
        return redirect('student:all_plans')
    return render(request, 'studyplan/studyplan_delete_all.html')

def view_plan_details(request, plan_id):
    plan = get_object_or_404(Plan, pk=plan_id)
    subject_plans = SubjectPlan.objects.filter(plan=plan)
    return render(request, 'studyplan/study_plan_detail.html', {'plan': plan, 'subject_plans': subject_plans})

def add_subject_plan(request, plan_id):
    plan = get_object_or_404(Plan, pk=plan_id)
    if request.method == 'POST':
        form = SubjectPlanForm(request.POST)
        if form.is_valid():
            subject_plan = form.save(commit=False)
            subject_plan.plan = plan
            subject_plan.save()
        return redirect('student:view_plan_details', plan_id=plan.pk)
        SubjectPlan.objects.filter(plan=plan, cycle='общеобразовательное').update(number=models.F('number') + 1)
        new_subject.save()
    else:
        form = SubjectPlanForm()
    return render(request, 'studyplan/studyplan_form.html', {'form': form, 'plan': plan})

def edit_subject_plan(request, subject_plan_id):
    subject_plan = get_object_or_404(SubjectPlan, pk=subject_plan_id)
    if request.method == 'POST':
        form = SubjectPlanForm(request.POST, instance=subject_plan)
        if form.is_valid():
            form.save()
            return redirect('student:view_plan_details', plan_id=subject_plan.plan.pk)
    else:
        form = SubjectPlanForm()
    return render(request, 'studyplan/edit_subject_plan.html', {'form': form, 'subject_plan': subject_plan})

def delete_subject_plan(request, subject_plan_id):
    subject_plan = get_object_or_404(SubjectPlan, pk=subject_plan_id)
    plan_id = subject_plan.plan.pk
    if request.method == 'POST':
        subject_plan.delete()
        return redirect('student:view_plan_details', plan_id=plan_id)
    return render(request, 'studyplan/delete_subject_plan.html', {'subject_plan': subject_plan})

