from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth


# Create your views here.
def login(request):
    if request.method=='POST':
        user_name=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=user_name,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid user')

    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        user_name=request.POST['username']
        f_name = request.POST['first_name']
        l_name = request.POST['last_name']
        email = request.POST['email']
        pass1=request.POST['password']
        cpass = request.POST['password1']
        if pass1==cpass:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,"Username already exists")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already exists")
                return redirect("register")
            else:
                user=User.objects.create_user(username=user_name,first_name=f_name,last_name=l_name,email=email,password=pass1)
                user.save()
                print("User Created")
                return redirect("login")
        else:
            messages.info(request,"Password mismatch")
            return redirect("register")


        return redirect("/")

    return render(request,'registration.html')

def logout(request):
    auth.logout(request)
    return redirect('/')