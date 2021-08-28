from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
from Products.models import Category, Product, Brand
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
        return render(request, "Products.html", {'email': email, 'categories': categories, 'brands': brands, 'products': products, 'category': category})
    else:
        return redirect('/')


# Filtering by category function


def Categoryfilter(request):
    email = request.user.email
    categories = Category.objects.all()
    brands = Brand.objects.all()
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
    brandid = request.GET.get('brand')
    global categoryID
    if categoryID == 0:
        products = Product.objects.filter(brand_id=brandid)
    else:
        products = Product.objects.filter(
            category_id=categoryID, brand_id=brandid)

    return render(request, "Products.html", {'email': email, 'categories': categories, 'brands': brands, 'products': products, 'category': category})

# Logout function


def Logout(request):
    logout(request)
    return redirect('/')
