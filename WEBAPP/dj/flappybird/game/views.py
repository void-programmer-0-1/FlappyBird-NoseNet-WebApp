from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .form import UserRegisterForm


def loginUser(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect("/game/home")
    
    else:

        if request.method == "POST":

            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                return HttpResponseRedirect("/game/home")
            else:
                messages.info(request,"Username or password is invalid")

        return render(request,"login.html")


def registerUser(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect("/game/home")
    
    else:

        form = UserRegisterForm()

        if request.method == "POST":
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get("username")
                messages.success(request,"Accout created for {}".format(username))
                return HttpResponseRedirect("/game/")

        return render(request,"register.html",{"form":form})


@login_required(login_url="/game/")
def logoutUser(request):
    logout(request)
    return HttpResponseRedirect("/game/")


@login_required(login_url="/game/")
def home(request):
    
    return render(request,"home.html",None)


@login_required(login_url="/game/")
def about(request):

    return render(request,"about.html",None)


@login_required(login_url="/game/")
def hand_game(request):

    return render(request,"hand_game.html",None)


@login_required(login_url="/game/")
def nose_game(request):
    
    return render(request,"nose_game.html",None)




