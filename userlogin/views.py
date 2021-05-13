from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import Register
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def index(request):
    return render (request, "index.html")
#@login_required(login_url='/accounts/login/')
def bookmark(request):
    return render (request, "Bookmarks.html") 

def login(request):
    return render (request, "login.html")

def password(request):
    return render (request, "password.html")
    

def register(request):
    form = UserCreationForm()
    if request.method == "post":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("Valodfpor")
            form.save()
            messages.success(request,message="Sucesuffely created")
            return redirect('login')


    return render(request,"registration/register.html",{'form':Register})

