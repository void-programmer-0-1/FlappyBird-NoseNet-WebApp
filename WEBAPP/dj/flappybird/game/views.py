from django.db import reset_queries
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .form import UserRegisterForm
from django.http import HttpResponse
from .models import ScoreBoard
from django.contrib.auth.models import User

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

    

    if request.method == "POST":
        game_score = int(request.POST.get("score"))
        user = User.objects.get(username=request.user.username)
        old_score = ScoreBoard.objects.get(user=user)

        if game_score > old_score.score:
            old_score.score = game_score
            old_score.save()

            return HttpResponse("Yeh You Now Achieved a New High Score {}".format(game_score), status=200)
        
        return HttpResponse("Try Harder Bitch !!!" ,status=200)

    return render(request,"hand_game.html",None)


@login_required(login_url="/game/")
def nose_game(request):
    
    return render(request,"nose_game.html",None)




