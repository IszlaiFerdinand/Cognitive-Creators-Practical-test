from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
from Products.models import Category, Product, Brand, CartItems
# Create your views here.

# rendering Products page function


@csrf_exempt
def Products(request):
    if request.user.is_authenticated:
        email = request.user.email
        categories = Category.objects.all()
        brands = Brand.objects.all()
        products = Product.objects.all()
        category = "All categories"
        global categoryID
        categoryID = 0
        global brandID
        brandID = 0
        return render(request, "Products.html", {'email': email, 'categories': categories, 'brands': brands, 'products': products, 'category': category})
    else:
        return redirect('/')


# Filtering by category function


def Categoryfilter(request):
    email = request.user.email
    categories = Category.objects.all()
    brands = Brand.objects.all()
    global brandID
    brandID = 0
    category_id = request.GET.get('category')
    global category
    category = Category.objects.get(id=category_id).name
    global categoryID
    categoryID = Category.objects.get(id=category_id).id
    products = Product.objects.filter(category_id=category_id)
    return render(request, "Products.html", {'email': email, 'categories': categories, 'brands': brands, 'products': products, 'category': category})


# Filtering by brand function


def Brandfilter(request):
    email = request.user.email
    categories = Category.objects.all()
    brands = Brand.objects.all()
    global brandID
    brandID = request.GET.get('brand')
    global categoryID
    if categoryID == 0:
        products = Product.objects.filter(brand_id=brandID)
    else:
        products = Product.objects.filter(
            category_id=categoryID, brand_id=brandID)

    return render(request, "Products.html", {'email': email, 'categories': categories, 'brands': brands, 'products': products, 'category': category})

# Logout function


def Logout(request):
    logout(request)
    return redirect('/')

# Add to cart function


def addtocart(request):
    if request.method == 'POST':
        email = request.user.email
        categories = Category.objects.all()
        brands = Brand.objects.all()
        quantity = request.POST['quantity']
        productID = request.POST['productID']
        userID = request.user.id
        if CartItems.objects.filter(user_id=userID, product_id=productID).exists():
            currentamount = CartItems.objects.get(
                user_id=userID, product_id=productID).quantity
            updatedamount = currentamount + int(quantity)
            updatelisting = CartItems.objects.get(
                user_id=userID, product_id=productID)
            updatelisting.quantity = updatedamount
            updatelisting.save()
        else:
            newadd = CartItems(product_id=productID,
                               quantity=quantity, user_id=userID)
            newadd.save()

        global categoryID
        global brandID
        global category
        if "categoryID" not in globals():
            categoryID = 0
        if "brandID" not in globals():
            brandID = 0
        if "category" not in globals():
            category = "All categories"
        currentstock = Product.objects.get(id=productID).onstock
        updatedstock = currentstock - int(quantity)
        updateproduct = Product.objects.get(id=productID)
        updateproduct.onstock = updatedstock
        updateproduct.save()
        # Creating the product listing based on previous search
        if categoryID == 0 and brandID == 0:
            products = Product.objects.all()
        elif categoryID != 0 and brandID == 0:
            products = Product.objects.filter(category_id=categoryID)
        elif categoryID == 0 and brandID != 0:
            products = Product.objects.filter(brand_id=brandID)
        else:
            products = Product.objects.filter(
                category_id=categoryID, brand_id=brandID)
        return render(request, "Products.html", {'email': email, 'categories': categories, 'brands': brands, 'products': products, 'category': category})
