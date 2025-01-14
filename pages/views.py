from django.shortcuts import render
from django.http import HttpResponse
from .models import Login
from .forms import LoginForm

# Create your views here.
def index(request):
    # return HttpResponse("Hi there")
    info={'name':['bayan','batoul']}
    return render(request , 'pages/index.html' ,info )


def about(request):
    # username=request.POST.get('username')
    # password=request.POST.get('password')
    # data=Login(username=username,password=password)
    # data.save()


    LoginForm(request.Post).save()
    return render(request,'pages/about.html',{'lf':LoginForm})