from django.shortcuts import render
from Products.models import Category, Product, Brand, CartItems, Order
from . import views
# Create your views here.

# Checkout page rendering -> function


def Checkout(request):
    if request.user.is_authenticated:
        userID = request.user.id
        cart = CartItems.objects.select_related(
            'product').filter(user_id=userID, ordered=False)
        totalamount = 0
        for item in cart.iterator():
            totalamount += item.quantity*item.product.price

        totalwithVAT = totalamount*1.19
        # Checking if the QuerySet is empty or not
        if cart.exists():
            empty = False
        else:
            empty = True

        return render(request, 'Checkout.html', {'cart': cart, 'totalamount': totalamount, 'totalwithVAT': totalwithVAT, 'empty': empty})
    else:
        return redirect('/')

# Removing items from cart -> function


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

# Finalize order function


def Finalize(request):
    if request.method == 'POST':
        # getting the data from completed form
        usertype = request.POST['type']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        adress = request.POST['adress']
        iban = request.POST['iban']
        bank = request.POST['bank']
        registrationnumber = request.POST['reg']
        delivery = request.POST['delivery']
        payment = request.POST['payment']
        comments = request.POST['comment']
        userID = request.user.id
        cart = CartItems.objects.select_related(
            'product').filter(user_id=userID, ordered=False)
        totalamount = 0
        # calculating the totalamount and setting >ordered< field to True, so we can still access the ordered items, but they will not appear in cart
        for item in cart.iterator():
            totalamount += item.quantity*item.product.price
            item.ordered = True
            item.save()

        totalwithVAT = totalamount*1.19
        # adding a new record to Order table
        newadd = Order(user_id=userID, usertype=usertype, firstname=firstname, lastname=lastname, email=email, adress=adress, iban=iban,
                       bank=bank, registrationnumber=registrationnumber, delivery=delivery, payment=payment, comments=comments, totalamount=totalwithVAT)
        newadd.save()

        return render(request, "Thanks.html")
    else:
        return redirect('/')
