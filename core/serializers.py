#PACKAGE IMPORTS
from rest_framework import serializers
from django.contrib.auth.models import User
from django.forms import HiddenInput

#LOCAL IMPORTS
from core.models import Auto


class UserSerializer(serializers.ModelSerializer):
    """ Serializer for auth API """
    class Meta:
        model = User
        fields = ("__all__")
        
class AutoSerializer(serializers.ModelSerializer):
    """ Serializer for auto API """
    class Meta:
        model = Auto
        fields = ("__all__")