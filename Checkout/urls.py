from django.urls import path
from . import views

urlpatterns = [
    path('Checkout', views.Checkout, name='Checkout'),
    path('Removefromcart', views.Removefromcart, name='Removefromcart'),
]
