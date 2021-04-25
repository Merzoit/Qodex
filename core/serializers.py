#PACKAGE IMPORTS
from rest_framework import serializers
from django.contrib.auth.models import User
from django.forms import HiddenInput

#LOCAL IMPORTS
from core import models

"""

class Name(serializers.ModelSerializer):
    class Meta:
        model = modelname
        fields = ('__all__')

Name - имя сериализера.
serializers.ModelSerializer - наследование от класса rest_framework, принимает параметры:
    1. model - модель Python для JSON-API
    2. fields - поля модели, для JSON-API. 
        ('__all__') - все поля моделию
        Альтернатива:
        ('fieldsname1','fieldsname2','fieldsname3')

"""

class UserSerializer(serializers.ModelSerializer):
    """ Serializer for API """
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

class OperatorsSerializer(serializers.ModelSerializer):
    """ Serializer for API """
    class Meta:
        model = models.Operators
        fields = ("__all__")

class Qodex_achiveSerializer(serializers.ModelSerializer):
    """ Serializer for API """
    class Meta:
        model = models.Qodex_achive
        fields = ("__all__")

class Cm_events_logSerializer(serializers.ModelSerializer):
    """ Serializer for API """
    class Meta:
        model = models.Cm_events_log
        fields = ("__all__")

class RFID_IDSerializer(serializers.ModelSerializer):
    """ Serializer for API """
    class Meta:
        model = models.RFID_ID
        fields = ("__all__")

class RFID_typesSerializer(serializers.ModelSerializer):
    """ Serializer for API """
    class Meta:
        model = models.RFID_types
        fields = ("__all__")

class Qodex_usersSerializer(serializers.ModelSerializer):
    """ Serializer for API """
    class Meta:
        model = models.Qodex_users
        fields = ("__all__")

class RegionsSerializer(serializers.ModelSerializer):
    """ Serializer for API """
    class Meta:
        model = models.Regions
        fields = ("__all__")

class Codex_orgSerializer(serializers.ModelSerializer):
    """ Serializer for API """
    class Meta:
        model = models.Qodex_org
        fields = ("__all__")

class Oro_infoSerializer(serializers.ModelSerializer):
    """ Serializer for API """
    class Meta:
        model = models.Oro_info
        fields = ("__all__")

class User_rolesSerializer(serializers.ModelSerializer):
    """ Serializer for API """
    class Meta:
        model = models.User_roles
        fields = ("__all__")