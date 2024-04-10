from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("nfps/", views.nfps, name="NFPs"),
    path("contactus/", views.contactus, name="Contact Us"),
    path("success/", views.successView, name='success'),
    path("register/", views.registerPage, name = "register"),
    path("login/", views.loginPage, name = "login"),
    path("logout/", views.logoutUser, name="logout"),
    path("grant_application", views.grantApplication, name="Grant Application"),
    path('createGrantModelForm', views.createGrantModelForm, name="Create Grant"),
]