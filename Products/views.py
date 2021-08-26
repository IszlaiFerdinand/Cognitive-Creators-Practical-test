from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def Products(request):
    # if request.method == 'POST':
    return render(request, "Products.html")
    # else:
    #     return render(request, './Login.html')
