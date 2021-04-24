#PACKAGE IMPORT
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

#LOCAL IMPORT
from core import views

urlpatterns = [
   path('api/user', views.Login.as_view()),
   path('api/auto', views.AutoView.as_view()),
   path('api/trash_types', views.Trash_typesViews.as_view()),
   path('api/trash_cats', views.Trash_catsViews.as_view()),
   path('api/weight_types', views.Weight_typesViews.as_view()),
]
