from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from.forms import ItemForm,RegisterForm,DetailEditForm
from.models import item,UserDetails
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
# Create your views here.


def home_view(request):
    form=ItemForm()
    if request.method=="POST":
        form=ItemForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('e_commerce_app:list')
    return render(request,'home.html',{'form':form})

def list(request):
    data=item.objects.all()
    return render(request,'list.html',{"data":data})   

def details(request,id):
    data=item.objects.get(id=id)

    return render(request,'details.html',{"data":data})    



def login_view(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        myuser=authenticate(username=username,password=password)
        print(myuser)
        if myuser is not None:
            print("logged in")
            login(request,myuser)
            return redirect('/')
    # form=LoginForm()            
    return render(request,'login.html')


def register_view(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if request.method=="POST":
            username=request.POST['username']
            password=request.POST['password']
            email=request.POST['email']
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            address=request.POST['address']
            phone_no=request.POST['phone_no']
            myuser=UserDetails.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name,address=address,phone_no=phone_no)
            print(myuser)
            myuser.save()
            return redirect('e_commerce_app:login')
    form=RegisterForm()      
    return render(request,'register.html',{"form":form})



def choice(request):
    return render(request,"choice.html")


def logout_view(request):
    logout(request)
    return redirect('e_commerce_app:list')



def buy_view(request,id):
    data=request.user
    return render(request,'buy.html',{"data":data})


def edit_view(request,id):
    data=request.user
    form=DetailEditForm()
    if request.method=="POST":
        form=request.POST
        data.first_name=request.POST['first_name']
        data.last_name=request.POST['last_name']
        data.address=request.POST['address']
        data.email=request.POST['email']
        data.phone_no=request.POST['phone_no']
        data.save()
        print(id)
        # return redirect('buy' , id=id)
        return redirect("e_commerce_app:buy", id)

        # return HttpResponse("details changed go back")
    return render(request,'edit.html',{"form":form})


def wish_view(request):
    return HttpResponse("Congratulations! Your Order Was Placed!")