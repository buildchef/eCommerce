from django.urls import path

from . import views

urlpatterns = [
    path('', views.Pay.as_view(), name='pay'),
    path('closeorder/', views.CloseOrder.as_view(), name='closeorder'),
    path('detail/', views.Detail.as_view(), name='detail'),
]
