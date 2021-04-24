#PACKAGE IMPORT
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
#LOCAL IMPORT
from core.serializers import UserSerializer, AutoSerializer
from core.models import Auto

#API
class Login(generics.ListCreateAPIView):
    """ API for USER """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AutoView(generics.ListCreateAPIView):
    """ API for Auto """
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer