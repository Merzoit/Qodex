#PACKAGE IMPORT
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

#LOCAL IMPORT
from core import views

urlpatterns = [
   path('api/user', views.Login.as_view()),
   path('password_change/', PasswordChangeView.as_view(), name='password_change')
]
