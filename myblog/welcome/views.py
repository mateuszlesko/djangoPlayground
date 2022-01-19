from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.http.response import Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User

# Create your views here.

def index(request):
    return render(request,"welcome/index.html",{})

def profile(request):
    content = {"profile":request.user}
    return render(request,"welcome/profile.html",content)

def mylogin(request):
    if request.method == "POST":
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("welcome/profile")
        else:
            return render(request,"welcome/login.html")
    else:
        return render(request,"welcome/login.html")

def mylogout(request):
    status = logout(request)  
    content = {"status":status}
    return render(request,"welcome/logout.html",content)


def changePassword(request):
    if request.method == "GET":
        return render(request,"welcome/changePassword.html")
    else:
        username  = request.user
        oldPassword = request.POST['oldPassword']
        user = authenticate(request, username=username, password=oldPassword)
        password1 = request.POST['newPassword1']
        password2 = request.POST['newPassword2']

        if user and (password1 == password2):
            user.set_password(password1)
            user.save()
            return redirect("welcome/profile")
        else:
            return render(request,"welcome/changePassword.html",{"ok":False})
