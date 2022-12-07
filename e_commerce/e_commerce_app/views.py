from django.shortcuts import render,redirect
from django.http import HttpResponse
from.forms import ItemForm,RegisterForm,LoginForm
from.models import item
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
# Create your views here.


def home_view(request):
    form=ItemForm()
    if request.method=="POST":
        form=ItemForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("list")
    return render(request,'home.html',{'form':form})

def list(request):
    data=item.objects.all()
    return render(request,'list.html',{"data":data})   

def checkout(request,id):
    data=item.objects.get(id=id)

    return render(request,'checkout.html',{"data":data})    



def login_view(request):
    context={}
    form=LoginForm()
    context['form']=form
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        myuser=authenticate(username=username,password=password)
        print(myuser)
        if myuser is not None:
            print("logged in")
            login(request,myuser)
            return redirect('/')
    return render(request,'login.html',context)


def register_view(request):
    context={}
    form=RegisterForm(request.POST)
    context['form']=form
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        myuser=User.objects.create_user(username=username,password=password,email=email)
        print(myuser)
        myuser.save()
        return redirect('login')
    return render(request,'register.html',context)



def choice(request):
    return render(request,"choice.html")
