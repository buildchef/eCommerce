from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from . import forms, models

# Create your views here.

class BaseProfile(View):
    template_name = '_profile/create.html'
    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.context = {
            'userform' : forms.UserForm(data=self.request.POST or None),
            'profileform' : forms.ProfileForm(data=self.request.POST or None) 
        }

        self.rendering = render(self.request, self.template_name, self.context)

    def get(self, *args, **kwargs):
        return self.rendering


class Create(BaseProfile):
    pass

class Update(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Update')
class Login(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Login')

class Logout(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Logout')