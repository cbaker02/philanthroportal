# main/urls.py
from django.contrib import admin
from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from main.views import ChangePasswordView


urlpatterns = [
    path("", views.home, name="Home"),
    path("nfps/", views.nfps, name="NFPs"),
    path("contactus/", views.contactus, name="Contact Us"),
    path("success/", views.successView, name='success'),
    path("register/", views.registerPage, name = "register"),
    path("nfpRegister", views.nfpRegister, name="NFP Register"),
    path("corpRegister", views.corpRegister, name="Corp Register"),
    path("login/", views.loginPage, name = "login"),
    path("logout/", views.logoutUser, name="logout"),
    path("grant_application", views.grantApplication, name="Grant Application"),
    path('create_grant', views.createGrant, name="Create Grant"),
    path('grant_list', views.grant_list, name="grant_list"),
    path('my_grants', views.my_grants, name="my_grants"),
    path('my_applications', views.my_applications, name="my_applications"),
    path('nfp_donation', views.nfp_donation, name="nfp_donation"),
    path('indv_donation', views.indv_donation, name="indv_donation"),
    path('make_donation', views.make_donation, name="Make Donation"),
    path('profile/', views.profile, name="users-profile"),
    path('password-change/', ChangePasswordView.as_view(),name="password_change"),
    re_path(r'^update_application_status/(?P<app_id>[0-9a-f-]+)/$', views.update_application_status, name='update_application_status')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)