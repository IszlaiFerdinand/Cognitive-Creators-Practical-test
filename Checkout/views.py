from django.shortcuts import render

# Create your views here.

# Checkout page render


def Checkout(request):
    if request.user.is_authenticated:
        return render(request, 'Checkout.html')
    else:
        return redirect('/')
