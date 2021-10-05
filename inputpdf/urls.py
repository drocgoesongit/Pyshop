from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('profile', views.profile, name="profile"),
    path('login', views.loginPage, name="login"),
    path('register', views.register, name="register")
]
