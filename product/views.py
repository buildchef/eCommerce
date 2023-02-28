from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView

# Create your views here.

class ListProducts(View):
    def get(self, *args, **kwargs):
        return HttpResponse('ListProducts')

class DetailProduct(View):
    def get(self, *args, **kwargs):
        return HttpResponse('DetailProduct')

class AddToCart(View):
    def get(self, *args, **kwargs):
        return HttpResponse('AddToCart')

class RemoveFromCart(View):
    def get(self, *args, **kwargs):
        return HttpResponse('RemoveFromCart')

class Cart(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Cart')

class Finalize(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finalize')