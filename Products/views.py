from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def Products(request):
    if request.method == 'POST':
        return HttpResponse("Products.html")
    else:
        return render(request, './Login.html')
