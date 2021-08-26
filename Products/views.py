from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
# Create your views here.


@csrf_exempt
def Products(request):
    return render(request, "Products.html")


def Logout(request):
    logout(request)
    return redirect('/')
