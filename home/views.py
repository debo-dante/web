from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.conf import settings

from django import forms


from .models import ProductInfo
from .forms import CreateUserForm
from .forms import ImageForm


# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')

    return render(request,'index.html')

def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            
            return redirect("/")
        else:
            return render(request,'login.html')
            

    return render(request,'login.html')

def signupuser(request):

    form = CreateUserForm()
    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
           form.save()
           user= form.cleaned_data.get('username')
           messages.success(request, "Account was created for "+ user)
           return redirect('login')
    
    context = {'form': form}

    return render(request,'signup.html',context)

def product_reg(request):
    if request.method == 'POST':
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            file_url=form.instance
            messages.success(request, "Product was successfully added to the database ")
            return redirect('/product_reg',{'file_url':file_url})

        
    else:
        form=ImageForm()
        
    return render(request,'product_reg.html',{'form':form})

def product_sell(request):
    if ProductInfo.objects.count()==0:
        messages.success(request, "There are no products available at the moment")
    if request.method == 'POST':
        search = request.POST.get('search')
        products = ProductInfo.objects.filter(itemname__startswith = search)
        if products.exists()==False:
            messages.success(request, "No products found ")
    else:
        products = ProductInfo.objects.all()

    return render(request,'product_sell.html',{'products':products})

def product_conf(request):
    if request.method == 'POST':
        send_mail('subject', 'body of the message', EMAIL_HOST_USER, [products.email])
        ProductInfo.objects.filter(sellername=)
        return render(request,'emailsent.html')

def logoutuser(request):
    logout(request)
    return redirect("/login")


