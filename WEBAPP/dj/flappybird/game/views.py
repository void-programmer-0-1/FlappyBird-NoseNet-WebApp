from django.shortcuts import render

# Create your views here.


def home(request):
    
    return render(request,"home.html",None)


def about(request):

    return render(request,"about.html",None)

def hand_game(request):

    return render(request,"hand_game.html",None)

def nose_game(request):
    
    return render(request,"nose_game.html",None)


