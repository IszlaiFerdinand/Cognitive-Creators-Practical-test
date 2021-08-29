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
        totalamount = 0
        for item in cart.iterator():
            totalamount += item.quantity*item.product.price

        totalwithVAT = totalamount*1.19
        return render(request, 'Checkout.html', {'cart': cart, 'totalamount': totalamount, 'totalwithVAT': totalwithVAT})
    else:
        return redirect('/')


def Removefromcart(request):
    cartitems_id = request.GET['remove']
    quantityobj = CartItems.objects.filter(id=cartitems_id).get()
    quantity = quantityobj.quantity
    product_idobj = CartItems.objects.filter(id=cartitems_id).get()
    product_id = product_idobj.product_id
    # adding back to stock removed products
    updateproduct = Product.objects.get(id=product_id)
    updateproduct.onstock += quantity
    updateproduct.save()
    # deleting selected cart item from database
    CartItems.objects.filter(id=cartitems_id).delete()
    return views.Checkout(request)
