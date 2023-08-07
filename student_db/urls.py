from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('about', views.about_us, name='about_us'),

    path('student/', views.student_list, name='student_list'),
    path('student/create/', views.student_create, name='student_create'),
    path('student/<int:pk>/update/', views.student_update, name='student_update'),
    path('student/<int:pk>/delete/', views.delete_student, name='delete_student'),
    path('student/filter/', views.student_filter, name='student_filter'),

    path('teacher/', views.teacher_list, name='teacher_list'),
    path('teacher/new/', views.teacher_new, name='teacher_new'),
    path('teacher/<int:pk>/update/', views.teacher_update, name='teacher_update'),
    path('teacher/<int:pk>/', views.teacher_delete, name='teacher_delete'),
    path('teacher/filter/', views.teacher_filter, name='teacher_filter'),

    path('speciality/', views.speciality_list, name='speciality_list'),
    path('speciality/create/', views.create_speciality, name='create_speciality'),
    path('speciality/<int:pk>/update/', views.speciality_update, name='speciality_update'),
    path('speciality/<int:pk>/', views.speciality_delete, name='speciality_delete'),
    path('speciality/filter/', views.speciality_filter, name='speciality_filter'),

    path('subject/', views.subject_list, name='subject_list'),
    path('subject/all', views.subject_all, name='subject_all'),
    path('subject/create/', views.subject_create, name='subject_create'),
    path('subject/<int:pk>/update/', views.subject_update, name='subject_update'),
    path('subject/filter/', views.subject_filter, name='subject_filter'),
    path('subject/<int:pk>/', views.delete_subject, name='delete_subject'),

    path('plan/plans', views.all_plans, name='all_plans'),
    path('plan/create', views.create_plan, name='create_plan'),
    path('plan/<int:pk>/detail', views.view_plan, name='view_plan'),
    path('plan/<int:pk>/edit', views.edit_plan, name='edit_plan'),
    path('plan/<int:pk>/delete', views.delete_plan, name='delete_plan'),
    path('plan/delete_all', views.delete_all_plans, name='delete_all_plans'),
    path('plan/<int:plan_id>/', views.view_plan_details, name='view_plan_details'),
    path('plan/<int:plan_id>/add_subject', views.add_subject_plan, name='add_subject_plan'),
    path('subject_plan/<int:subject_plan_id>/edit_subject', views.edit_subject_plan, name='edit_subject_plan'),
    path('subject_plan/<int:subject_plan_id>/delete_subject', views.delete_subject_plan, name='delete_subject_plan'),
]