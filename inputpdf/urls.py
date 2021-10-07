from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('profile', views.getStarted, name="profile"),
    path('login', views.loginPage, name="login"),
    path('register', views.register, name="register"),
    path('home', views.home, name="home"),
    path('getStarted', views.getStarted)
]
