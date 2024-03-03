from django.shortcuts import render, redirect
from . forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):
    return render(request, "index.html")

def register(request):
    msg = None
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = "users created"
            return redirect("login_view")
        else:
            msg = "form is not valid"
    else:
        form = SignUpForm()
    return render(request, "register.html", {"form" : form, "msg" : msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("homepage")
            else:
                msg = "invalid credentials"
        else:
            msg = "error validating form"
    return render(request, "login.html", {"form" : form, "msg" : msg})

def admin(request):
    return render(request,'admin.html')


def Patient(request):
    return render(request,'Patient.html')


def Doctor(request):
    return render(request,'Doctor.html')
