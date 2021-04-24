#PACKAGE IMPORTS
from rest_framework import serializers
from django.contrib.auth.models import User
from django.forms import HiddenInput

#LOCAL IMPORTS



class UserSerializer(serializers.ModelSerializer):
    """ Serializer for auth API """
    class Meta:
        model = User
        fields = ("__all__")
        