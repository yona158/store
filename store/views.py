from django.shortcuts import render,redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms

def category(request,foo):
    # the url don't accept spaces
    foo = foo.replace('-',' ')

    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'store/category.html', {'products':products, 'category':category})
    except:
        messages.success(request,("That Category Doesn't Exist..."))
        return redirect('home')


def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request,'store/product.html',{'product':product})


def home(request):
    products = Product.objects.all()
    return render(request,'store/home.html',{'products':products})

def about(request):
    return render(request,'store/about.html',{})

def login_user(request):
    if request.method == "POST":
        # username = request.POST["username"]
        # password = request.POST["password"]
        username = request.POST.get("username", "").strip()  # Use .get() to avoid KeyError
        password = request.POST.get("password", "").strip()  # Use .get() to avoid KeyError

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,('You have been logged in! ... Welcome'))
            return redirect('home')
        else:
            messages.success(request,('There was an error ... Please try again'))
            return redirect('login')


    else:
        return render(request,'store/login.html',{})


def logout_user(request):
    logout(request)
    messages.success(request,('You have been logged out'))
    return redirect('home')


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #login user 
            user = authenticate(request, username=username, password=password)
            login(request,user)
            messages.success(request,('You have Registered! ... Welcome'))
            return redirect('home')
        else:
            messages.success(request,('Whooops... There was a problem registering, please try again'))
            return redirect('register' )

    return render(request,'store/register.html',{'form':form})
