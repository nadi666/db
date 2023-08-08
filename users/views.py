from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.core.exceptions import ValidationError
from django.utils.http import urlsafe_base64_decode
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate,  login

from users.forms import UserCreationForm, AuthenticationForm
from users.utils import send_email_for_verify

User = get_user_model()


class MyLoginView(LoginView):
    form_class = AuthenticationForm


class EmailVerify(View):
    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)
        if user is not None and token_generator.check_token(user, token):
            user.email_verify = True
            user.save()
            login(request, user)
            return redirect('home')
        return redirect('invalid_verify')


class Register(View):
    template_name = 'registration/register.html'
    render(request, self.template_name, context)
