from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

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
            return render(request, 'Login1.html', {'name': name})
        else:
            return render(request, 'Register.html')
    else:
        return render(request, 'Login.html')

# Actual login function


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
            return render(request, 'Products.html')

        else:
            message = "Invalid password! Try again!"
            return render(request, 'Login1.html', {'name': name, 'message': message})

    else:
        return render(request, 'Login.html')


# Registration function


def Register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = first_name+last_name
        pw = request.POST['password']
        pw1 = request.POST['password1']

        if pw == pw1:
            user = User.objects.create_user(
                username=username, password=pw1, email=email, first_name=first_name, last_name=last_name)
            user.save()
            # print("User created")
            return render(request, 'Products.html')
        else:
            message = "Passwords are not matching!"
            return render(request, 'Register.html', {'message': message})

    else:
        return render(request, 'Login.html')
