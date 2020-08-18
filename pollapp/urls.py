from django.urls import path
from . import views


urlpatterns = [

    path("", views.home, name="home"),
    path("votes/<str:pk>/", views.votes, name="votes"),
    path("results/<str:pk>/", views.results, name="results"),
    path("chartvote/<str:pk>/", views.chartvote, name="chartvote"),

]