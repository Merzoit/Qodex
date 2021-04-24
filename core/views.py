#PACKAGE IMPORT
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
#LOCAL IMPORT
from core.serializers import UserSerializer

#API

class Login(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer