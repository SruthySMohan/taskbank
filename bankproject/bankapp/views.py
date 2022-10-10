from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from .models import Branches


def home(request):
    return render(request,"home.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method=='POST':
        Username=request.POST['Username']
        Password=request.POST['Password']
        user=auth.authenticate(Username=Username,Password=Password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        # else:
        #      messages.info(request,"invalid credentials")
        #     messages.info(request,"successfull login")
    return render(request,"login.html")
def register(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        Firstname = request.POST['Firstname']
        Lastname = request.POST['Lastname']
        email= request.POST['email']
        Password = request.POST['Password']
        Password1 = request.POST['Password1']
        if Password == Password1:
            if User.objects.filter(Username=Username).exists():
                messages.info(request,"Username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exists")
                return redirect('register')
            else:
               user = User.objects.create_user(Username=Username, Password=Password, Firstname=Firstname,
                                            Lastname=Lastname, email=email)
               user.save()
               return redirect('login')
              # print("User Created")
        else:
            messages.info(request,"password not matching")
            return redirect('register')
         # return redirect('/')
    return render(request, "register.html")
def detail(request):
    return  render(request,'detail.html')
def registerform(request):
    return render(request,'registerform.html')
def form(request):
    return render(request,'form.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def submit(request):

        return render(request,'submit.html')
def branch(request):
    b=Branches.objects.all()
    context={
        'b':b
    }
    return render(request,"index.html",context)