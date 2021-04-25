#PACKAGE IMPORT
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
#LOCAL IMPORT
from core import models
from core import serializers

#API

"""

class Name(generics.ListCreateAPIView):
    queryset = modelname.objects.all()
    serializer_class = serializers.Selializername

Name - имя вьюхи.
generics.ListCreateAPIView - наследование от класса rest_framework, принимает параметры:
    1. queryset - объекты модели для передачи API.
    2. serializer_class - сериализер для передачи.


"""

class Login(generics.ListCreateAPIView):
    """ API for USER """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class AutoView(generics.ListCreateAPIView):
    """ API for Auto """
    queryset = models.Auto.objects.all()
    serializer_class = serializers.AutoSerializer

class Weight_typesViews(generics.ListCreateAPIView):
    """ API for Weight_types """
    queryset = models.Weight_types.objects.all()
    serializer_class = serializers.Weight_typesSerializer

class Trash_typesViews(generics.ListCreateAPIView):
    """ API for Trash_types """
    queryset = models.Trash_types.objects.all()
    serializer_class = serializers.Trash_typesSerializer

class Trash_catsViews(generics.ListCreateAPIView):
    """ API for Trash_cats """
    queryset = models.Trash_cats.objects.all()
    serializer_class = serializers.Trash_catsSerializer

class OperatorsViews(generics.ListCreateAPIView):
    """ API for Operators """
    queryset = models.Operators.objects.all()
    serializer_class = serializers.OperatorsSerializer    

class Qodex_achiveViews(generics.ListCreateAPIView):
    """ API for Qodex_achive """
    queryset = models.Qodex_achive.objects.all()
    serializer_class = serializers.Qodex_achiveSerializer   
    
class Cm_events_logViews(generics.ListCreateAPIView):
    """ API for Cm_events_log """
    queryset = models.Cm_events_log.objects.all()
    serializer_class = serializers.Cm_events_logSerializer 

class RFID_IDViews(generics.ListCreateAPIView):
    """ API for RFID_types """
    queryset = models.RFID_ID.objects.all()
    serializer_class = serializers.RFID_IDSerializer 

class RFID_typesViews(generics.ListCreateAPIView):
    """ API for RFID_types """
    queryset = models.RFID_types.objects.all()
    serializer_class = serializers.RFID_typesSerializer

class Qodex_usersViews(generics.ListCreateAPIView):
    """ API for Qodex_users """
    queryset = models.Qodex_users.objects.all()
    serializer_class = serializers.Qodex_usersSerializer

class RegionsViews(generics.ListCreateAPIView):
    """ API for Regions """
    queryset = models.Regions.objects.all()
    serializer_class = serializers.RegionsSerializer

class Qodex_orgViews(generics.ListCreateAPIView):
    """ API for Codex_org """
    queryset = models.Qodex_org.objects.all()
    serializer_class = serializers.Codex_orgSerializer

class Oro_infoViews(generics.ListCreateAPIView):
    """ API for RFID_types """
    queryset = models.Oro_info.objects.all()
    serializer_class = serializers.Oro_infoSerializer

class User_rolesViews(generics.ListCreateAPIView):
    """ API for User_roles """
    queryset = models.User_roles.objects.all()
    serializer_class = serializers.User_rolesSerializer


    