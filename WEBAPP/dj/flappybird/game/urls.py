from django.urls import path
from . import views

app_name = "game"

urlpatterns = [
    path("", views.home,name="home"),
    path("about/",views.about,name="about"),
    path("hand-game/",views.hand_game,name="hand_game"),
    path("nose-game/",views.nose_game,name="nose_game"),
]