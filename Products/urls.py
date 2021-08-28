from django.urls import path

from . import views

urlpatterns = [
    path('Products', views.Products, name='Products'),
    path('Logout', views.Logout, name='Logout'),
    path('Brandfilter', views.Brandfilter, name='Brandfilter'),
    path('Categoryfilter', views.Categoryfilter, name='Categoryfilter')
]
