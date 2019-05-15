from django import forms
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from ToDoList.models import *
from django.utils.http import is_safe_url
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, RedirectView


class LoginView(FormView):

    success_url = '/main/'
    form_class = AuthenticationForm
    template_name = 'login.html'

    def form_valid(self, form):
        auth_login(self.request, form.get_user())

        return super(LoginView, self).form_valid(form)

class LogoutView(RedirectView):

    url = '/auth/login/'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)

class Home(LoginRequiredMixin, TemplateView):
    template_name = "main.html"
    login_url = "/login/"

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        
class RegisterView(FormView):
    success_url = '/login/'
    form_class = UserForm
    template_name = 'register.html'

    def form_valid(self, form):
        print("User Saved")
        form.save()
        return super(RegisterView, self).form_valid(form)
