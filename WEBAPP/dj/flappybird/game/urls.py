from django.urls import path
from . import views

app_name = "game"

urlpatterns = [
    path("home/", views.home,name="home"),
    path("about/",views.about,name="about"),
    path("hand-game/",views.hand_game,name="hand_game"),
    path("nose-game/",views.nose_game,name="nose_game"),
    path("",views.loginUser,name="loginUser"),
    path("register/",views.registerUser,name="registerUser"),
    path("logout/",views.logoutUser,name="logout"),
]