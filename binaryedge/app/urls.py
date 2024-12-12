from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    path('',views.index,name="home"),
    path('images/',views.image,name="images"),
    path('dataleaks/',views.dataleaks,name="dataleaks"),
    path('domains/',views.domains,name="domains"),
    path('sensors/',views.sensors,name="sensors"),
    path('torrents/',views.torrents,name="torrents"),
]
