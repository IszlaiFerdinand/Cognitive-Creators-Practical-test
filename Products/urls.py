from django.urls import path

from . import views

urlpatterns = [
    path('', views.Products, name='Products'),
]
