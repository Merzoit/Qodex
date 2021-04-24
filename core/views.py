#PACKAGE IMPORT
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
#LOCAL IMPORT
from core.serializers import UserSerializer, AutoSerializer, Weight_typesSerializer, Trash_catsSerializer, Trash_typesSerializer
from core.models import Auto, Weight_types, Trash_types, Trash_cats

#API
class Login(generics.ListCreateAPIView):
    """ API for USER """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AutoView(generics.ListCreateAPIView):
    """ API for Auto """
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer

class Weight_typesViews(generics.ListCreateAPIView):
    queryset = Weight_types.objects.all()
    serializer_class = Weight_typesSerializer

class Trash_typesViews(generics.ListCreateAPIView):
    queryset = Trash_types.objects.all()
    serializer_class = Trash_typesSerializer

class Trash_catsViews(generics.ListCreateAPIView):
    queryset = Trash_cats.objects.all()
    serializer_class = Trash_catsSerializer