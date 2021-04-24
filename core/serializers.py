#PACKAGE IMPORTS
from rest_framework import serializers
from django.contrib.auth.models import User
from django.forms import HiddenInput

#LOCAL IMPORTS
from core import models


class UserSerializer(serializers.ModelSerializer):
    """ Serializer for auth API """
    class Meta:
        model = User
        fields = ("__all__")
        
class AutoSerializer(serializers.ModelSerializer):
    """ Serializer for API """
    class Meta:
        model = models.Auto
        fields = ("__all__")

class Weight_typesSerializer(serializers.ModelSerializer):
    """ Serializer for API """
    class Meta:
        model = models.Weight_types
        fields = ("__all__")

class Trash_typesSerializer(serializers.ModelSerializer):
    """ Serializer for API """
    class Meta:
        model = models.Trash_types
        fields = ("__all__")

class Trash_catsSerializer(serializers.ModelSerializer):
    """ Serializer for API """
    class Meta:
        model = models.Trash_cats
        fields = ("__all__")