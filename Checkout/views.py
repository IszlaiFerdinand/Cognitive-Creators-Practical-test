from django.shortcuts import render
from Products.models import Category, Product, Brand, CartItems
from . import views
# Create your views here.

# Checkout page render


def Checkout(request):
    if request.user.is_authenticated:
        userID = request.user.id
        cart = CartItems.objects.select_related(
            'product').filter(user_id=userID)
        return render(request, 'Checkout.html', {'cart': cart})
    else:
        return redirect('/')


def Removefromcart(request):
    cartitems_id = request.GET['remove']
    CartItems.objects.filter(id=cartitems_id).delete()
    print(cartitems_id)
    print("Success")
    return views.Checkout(request)
