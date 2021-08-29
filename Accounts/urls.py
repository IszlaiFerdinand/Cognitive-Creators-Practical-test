from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home),
    path('Login', views.Login, name='Login'),
    path('Register', views.Register, name='Register'),
    path('Login1', views.Login1, name='Login1')
]
