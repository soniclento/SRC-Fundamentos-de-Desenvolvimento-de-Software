from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.models import User
from django.contrib import messages

def signup(request):

    if request.method == "POST":
        
        username1 = request.POST["username"]
        email1 = request.POST["email"]
        password = request.POST["password"]
        password1 = request.POST["password1"]

        if password == password1:

            if User.objects.filter(email = email1).exists():
                messages.info(request,"Email already exists")
                return redirect("signup")
            elif User.objects.filter(username = username1).exists():
                messages.info(request,"Username already exists")
                return redirect("signup")
            else:
                user= User.objects.create_user(username=username1,email=email1,password=password)
                user.save()
                return redirect("login")
        
        else:
            messages.info(request," Password not the same")
            return redirect("signup")
    
    else:
        return render(request, "auth_src/signup.html")

def login(request):

    if request.method == "POST":
        user_name = request.POST["username"]
        user_password = request.POST["password"]

        user = authenticate(username=user_name, password=user_password)
        if user is not None:
            django_login(request,user)
            return redirect("plataforma")
        else:
            messages.info(request,"Invalid credentials")
            return redirect("login")
    else:
        return render(request, "auth_src/login.html")

def plataforma(request):
    if request.user.is_authenticated:  
        return render(request, 'auth_src/plataforma.html')
    else:
        messages.info(request,"Please login first")
        return redirect("login")