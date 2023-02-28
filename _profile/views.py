from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

# Create your views here.

class Create(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Create')

class Update(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Update')
class Login(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Login')

class Logout(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Logout')