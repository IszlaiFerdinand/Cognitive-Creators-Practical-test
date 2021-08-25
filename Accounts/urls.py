from django.urls import path

from . import views

urlpatterns = [
    path('', views.Login, name='Login'),
    path('Login', views.Login, name='Login'),
    path('Register', views.Register, name='Register')
]
