from django.urls import path, include
from django.views.generic import TemplateView
from users.views import Register, EmailVerify, MyLoginView

urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),

    path('', include('django.contrib.auth.urls')),

    path('invalid_verify/',
         TemplateView.as_view(template_name='registration/invalid_verify.html'),
         name='invalid_verify'
         ),

    path('verify_email',
         EmailVerify.as_view(),
         name='email_verify',
         ),

    path('confirm_email/',
         TemplateView.as_view(template_name='registration/confirm_email.html')
         ),

    path('register/', Register.as_view(), name='register'),
]
