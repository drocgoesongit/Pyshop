from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('profile', views.getStarted, name="profile"),
    path('login', views.loginPage, name="login"),
    path('register', views.register, name="register"),
    path('home', views.home, name="home"),
    path('getStarted', views.getStarted),
    path('parserOutput', views.parser, name="parserOutput")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
