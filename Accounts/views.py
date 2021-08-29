from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from Products.models import Category, Product, Brand
# Create your views here.

# home page


def Home(request):
    return render(request, 'Index.html')


# Email check function


def Login(request):
    if request.method == 'POST':
        global email
        email = request.POST.get("email")

        if User.objects.filter(email=email).exists():
            # print('Email taken!')
            obj = User.objects.get(email=email)
            field_name = "first_name"
            field_value = getattr(obj, field_name)
            global name
            name = field_value
            return render(request, 'Login.html', {'name': name})
        else:
            return render(request, 'Register.html')
    else:
        return redirect('/')

# Actual login function


@csrf_exempt
def Login1(request):
    if request.method == 'POST':
        password = request.POST['password']
        obj = User.objects.get(email=email)
        field_name = "username"
        field_value = getattr(obj, field_name)
        user = auth.authenticate(username=field_value, password=password)
        # print(user)
        if user is not None:
            auth.login(request, user)
            categories = Category.objects.all()
            brands = Brand.objects.all()
            products = Product.objects.all()
            category = "All categories"
            return render(request, 'Products.html', {'email': email, 'categories': categories, 'brands': brands, 'products': products, 'category': category})

        else:
            message = "Invalid password! Try again!"
            return render(request, 'Login.html', {'name': name, 'message': message})

    else:
        return redirect('/')


# Registration function


@csrf_exempt
def Register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = email
        pw = request.POST['password']
        pw1 = request.POST['password1']

        if pw == pw1:
            user = User.objects.create_user(
                username=username, password=pw1, email=email, first_name=first_name, last_name=last_name)
            user.save()
            user = auth.authenticate(username=username, password=pw1)
            auth.login(request, user)
            categories = Category.objects.all()
            brands = Brand.objects.all()
            products = Product.objects.all()
            category = "All categories"
            return render(request, 'Products.html', {'email': email, 'categories': categories, 'brands': brands, 'products': products, 'category': category})
        else:
            message = "Passwords are not matching!"
            return render(request, 'Register.html', {'message': message})

    else:
        return redirect('/')
