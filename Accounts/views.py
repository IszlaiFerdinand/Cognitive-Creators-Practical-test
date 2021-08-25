from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
# Create your views here.


def Login(request):
    if request.method == 'POST':
        global email
        email = request.POST.get("email")

        if User.objects.filter(email=email).exists():
            print('Email taken!')
            obj = User.objects.get(email=email)
            field_name = "first_name"
            field_value = getattr(obj, field_name)
            name = field_value
            return render(request, 'Login1.html', {'name': name})
        else:
            print('Email free!')
            return render(request, 'Register.html')
    else:
        return render(request, 'Login.html')


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
            print("User created")
            return redirect('/')
        else:
            print("Passwords not matching")
            return render(request, 'Register.html')

    else:
        return render(request, 'Register.html')
