#PACKAGE IMPORT
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

#LOCAL IMPORT
from core import views

urlpatterns = [
   #API URLS
   path('api/user', views.Login.as_view()),
   path('api/auto', views.AutoView.as_view()),
   path('api/trash_types', views.Trash_typesViews.as_view()),
   path('api/trash_cats', views.Trash_catsViews.as_view()),
   path('api/weight_types', views.Weight_typesViews.as_view()),
   path('api/rfid', views.RFID_IDViews.as_view()),
   path('api/rfid_types', views.RFID_typesViews.as_view()),
   path('api/regions', views.RegionsViews.as_view()),
   path('api/oro_info', views.Oro_infoViews.as_view()),
   path('api/cm_events', views.Cm_events_logViews.as_view()),
   path('api/qodex_achive', views.Qodex_achiveViews.as_view()),
   path('api/user_roles', views.User_rolesViews.as_view()),
   path('api/qodex_org', views.Qodex_orgViews.as_view()),
   path('api/operators', views.OperatorsViews.as_view()),
   path('api/qodex_users', views.Qodex_usersViews.as_view()),
]
