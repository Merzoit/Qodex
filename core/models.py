#PACKAGE IMPORTS
from django.db import models

#LOCAL IMPORTS


class Auto(models.Model):
    """ Auto - model of auto databases """
    #RELATED FIELDS
    auto_model = models.ForeignKey('Auto_model', db_column='auto_model', blank=True, null=True)
    rfid_id = models.ForeignKey('RFID_ID', db_column='rfid_id', blank=True, null=True)
    poligon = models.ForeignKey('Poligon', db_column='poligon', blank=True, null=True)
    #LOCAL FIELDS
    car_number = models.CharField(unique=True, max_length=9, blank=True, null=True)
    id_type = models.CharField(max_length=10, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    rg_weight = models.IntegerFields(blank=True, null=True)
    awg_weight = models.IntegerFields(blank=True, null=True)
    ex_id = models.CharField(max_length=12, blank=True, null=True)
    upd_time = models.DateTimeField(blank=True, null=True)
    ar_get = models.DateTimeField(blank=True, null=True)
   
    class Meta:
        """ Model configurations """
        managed = True
        db_table = 'Auto'



class Auto_model(models.Model):
    """ Auto_model - model of auto_model databases """
    #RELATED FIELDS
    brand = models.ForeignKey('Auto_brands', db_column='auto_brands', blank=True, null=True)
    #LOCAL FIELDS
    name = models.CharField(max_length=60, blank=True, null=True)
    passport_mass = models.IntegerFields(blank=True, null=True)

    class Meta:
        """ Model configurations """
        managed = True
        db_table = 'Auto_model'




class Auto_brands(models.Model):
     """ Auto_brands - model of auto_brands databases """
     #LOCAL FIELDS
     name = models.CharField(max_length=20, blank=True, null=True)