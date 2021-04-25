#PACKAGE IMPORTS
from django.db import models

#LOCAL IMPORTS


class Qodex_users(models.Model):
    """ Qodex_users - model of Qodex_users databases """
    #RELATED FIELDS
    qodex_org = models.ForeignKey('Qodex_org', db_column='qodex_org', on_delete=models.SET_NULL, blank=True, null=True)
    role = models.ForeignKey('User_roles', db_column='user_roles', on_delete=models.SET_NULL, blank=True, null=True)
    region = models.ForeignKey('Regions', db_column='regions', on_delete=models.SET_NULL, blank=True, null=True)
    #LOCAL FIELDS
    name = models.TextField(blank=True, null=True)
    password = models.CharField(max_length=256, blank=True, null=True)
    refresh_token = models.TextField(blank=True, null=True)
    last_ip = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=120, blank=True, null=True)
    weight_fault = models.IntegerField(blank=True, null=True)
    connected = models.BooleanField(blank=True, null=True)
    inn = models.CharField(max_length=20, blank=True, null=True)
    kpp = models.CharField(max_length=20, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    def __str__(self):
        """ Django-admin UI """
        return self.name
    class Meta:
        """ Model configurations """
        managed = True
        db_table = 'Qodex_users'

class Auto(models.Model):
    """ Auto - model of auto databases """
    #RELATED FIELDS
    auto_model = models.ForeignKey('Auto_model', db_column='auto_model', on_delete=models.SET_NULL, blank=True, null=True)
    rfid_id = models.ForeignKey('RFID_ID', db_column='rfid_id', on_delete=models.SET_NULL, blank=True, null=True)
    poligon = models.ForeignKey('Qodex_users', db_column='poligon', on_delete=models.SET_NULL, blank=True, null=True)
    #LOCAL FIELDS
    car_number = models.CharField(unique=True, max_length=9, blank=True, null=True)
    id_type = models.CharField(max_length=10, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    rg_weight = models.IntegerField(blank=True, null=True)
    awg_weight = models.IntegerField(blank=True, null=True)
    ex_id = models.CharField(max_length=12, blank=True, null=True)
    upd_time = models.DateTimeField(blank=True, null=True)
    ar_get = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        """ Django-admin UI """
        return self.car_number
    class Meta:
        """ Model configurations """
        managed = True
        db_table = 'Auto'

class Auto_model(models.Model):
    """ Auto_model - model of auto_model databases """
    #RELATED FIELDS
    brand = models.ForeignKey('Auto_brands', db_column='auto_brands', on_delete=models.SET_NULL, blank=True, null=True)
    #LOCAL FIELDS
    name = models.CharField(max_length=60, blank=True, null=True)
    passport_mass = models.IntegerField(blank=True, null=True)
    def __str__(self):
        """ Django-admin UI """
        return self.name
    class Meta:
        """ Model configurations """
        managed = True
        db_table = 'Auto_model'

class Auto_brands(models.Model):
    """ Auto_brands - model of auto_brands databases """
    #LOCAL FIELDS
    name = models.CharField(max_length=20, blank=True, null=True)
    def __str__(self):
        """ Django-admin UI """
        return self.name
    class Meta:
        """ Model configurations """
        managed = True
        db_table = 'Auto_brands'    
    
class RFID_ID(models.Model):
    """ RFID_ID - model of RFID_ID databases """
    #RELATED FIELDS
    rfid_type = models.ForeignKey('RFID_types', db_column='rfid_types', on_delete=models.SET_NULL, blank=True, null=True)
    owner_id = models.ForeignKey('Qodex_users', db_column='qodex_users', on_delete=models.SET_NULL, blank=True, null=True)
    #LOCAL FIELDS
    rfid = models.CharField(max_length=20, blank=True, null=True)
    def __str__(self):
        """ Django-admin UI """
        return self.rfid
    class Meta:
        """ Model configurations """
        managed = True
        db_table = 'RFID_ID'

class RFID_types(models.Model):
    """ RFID_types - model of RFID_types """
    #LOCAL FIELDS
    name = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        """ Django-admin UI """
        return self.name
    class Meta:
        """ Model configurations """
        managed = True
        db_table = 'RFID_types'

class Weight_types(models.Model):
    """ Weight_types - model of weight_types databases """
    #LOCAL FIELDS
    name = models.TextField(blank=True, null=True)
    def __str__(self):
        """ Django-admin UI """
        return self.name
    class Meta:
        """ Model configurations """
        managed = True
        db_table = 'Weight_types'

class Trash_types(models.Model):
    """ Trash_types - model of trash_types databases """
    #RELATED FIELDS
    category = models.ForeignKey('Trash_cats', db_column='category', on_delete=models.SET_NULL, blank=True, null=True)
    poligon = models.ForeignKey('Qodex_users', db_column='poligon', on_delete=models.SET_NULL, blank=True, null=True)
    #LOCAL FIELDS
    name = models.TextField(blank=True, null=True)
    ex_id = models.IntegerField(blank=True, null=True)
    ar_get = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    def __str__(self):
        """ Django-admin UI """
        return self.name
    class Meta:
        """ Model configurations """
        managed = True
        db_table = 'Trash_types'
        
class Trash_cats(models.Model):
    """ Trash_cats - model of Trash_cats databases """
    #RELATED FIELDS
    poligon = models.ForeignKey('Qodex_users', db_column='poligon', on_delete=models.SET_NULL, blank=True, null=True)
    #LOCAL FIELDS
    category = models.TextField(blank=True, null=True)
    ex_id = models.IntegerField(blank=True, null=True)
    ar_get = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    def __str__(self):
        """ Django-admin UI """
        return self.category
    class Meta:
        """ Model configurations """
        managed = True
        db_table = 'Trash_cats'
        
class User_roles(models.Model):
    """ User_roles - model of User_roles databases """
    #LOCAL FIELDS
    name = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        """ Django-admin UI """
        return self.name
    class Meta:
        """ Model configurations """
        managed = True
        db_table = 'User_roles'

class Qodex_org(models.Model):
    """ Qodex_org - model of Qodex_org databases """
    #RELATED FIELDS
    region = models.ForeignKey('Regions', db_column='region', on_delete=models.SET_NULL, blank=True, null=True)
    #LOCAL FIELDS
    name = models.CharField(max_length=50, blank=True, null=True)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    inn = models.CharField(max_length=10, blank=True, null=True)
    kpp = models.CharField(max_length=20, blank=True, null=True)
    adress = models.CharField(max_length=200, blank=True, null=True)
    tel = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    dirrector = models.CharField(max_length=60, blank=True, null=True)
    org_type = models.CharField(max_length=30, blank=True, null=True)
    date_lic = models.DateTimeField(blank=True, null=True)
    lic_status = models.BooleanField(blank=True, null=True)
    def __str__(self):
        """ Django-admin UI """
        return self.name
    class Meta:
        """ Model configurations """
        managed = True
        db_table = 'Qodex_org'

class Operators(models.Model):
    """ Operators - model of operators databases """
    #RELATED FIELDS
    poligon = models.ForeignKey('Qodex_users', db_column='poligon', on_delete=models.SET_NULL, blank=True, null=True)
    #LOCAL FIELDS
    username = models.TextField(blank=True, null=True)  
    password = models.TextField(blank=True, null=True)  
    role = models.CharField(max_length=30, blank=True, null=True)
    fullname = models.CharField(max_length=30, blank=True, null=True)
    ex_id = models.IntegerField(blank=True, null=True)
    upd_time = models.DateTimeField(blank=True, null=True)
    ar_get = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    def __str__(self):
        """ Django-admin UI """
        return self.username
    class Meta:
        """ Model configurations """
        managed = True
        db_table = 'Operators'

class Qodex_achive(models.Model):
    """ Qodex_achive - model of qodex_achive databases """
    #RELATED FIELDS
    #table = models.ForeignKey('None', db_column='table', on_delete=models.SET_NULL, blank=True, null=True)
    poligon = models.ForeignKey('Qodex_users', db_column='poligon', on_delete=models.SET_NULL, blank=True, null=True)
    #LOCAL FIELDS
    date = models.DateTimeField(blank=True, null=True)
    user = models.CharField(max_length=20, blank=True, null=True)
    origin = models.TextField(blank=True, null=True) 
    new_data = models.TextField(blank=True, null=True) 
    restored = models.BooleanField(blank=True, null=True)
    restored_date = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        """ Django-admin UI """
        return self.user
    class Meta:
        """ Model configurations """
        managed = True
        db_table = 'Qodex_achive'

class Cm_events_log(models.Model):
    """ Cm_events_log - model of m_events_log databases """
    #RELATED FIELDS
    poligon = models.ForeignKey('Qodex_users', db_column='poligon', on_delete=models.SET_NULL, blank=True, null=True)
    #LOCAL FIELDS
    datetime = models.DateTimeField(blank=True, null=True)
    event = models.IntegerField(blank=True, null=True)
    operator = models.CharField(max_length=12, blank=True, null=True)
    ex_id = models.IntegerField(blank=True, null=True)
    upd_time = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        """ Django-admin UI """
        return self.operator
    class Meta:
        """ Model configurations """
        managed = True
        db_table = 'Cm_events_log'

class Regions(models.Model):
    """ Regions - model of regions databases """
    #LOCAL FIELDS
    name = models.CharField(max_length=30, blank=True, null=True)
    discription = models.TextField(blank=True, null=True)
    def __str__(self):
        """ Django-admin UI """
        return self.name
    class Meta:
        """ Model configuration """
        managed = True
        db_table = 'Regions'

class Oro_info(models.Model):
    """ Oro_info - model of oro_info databases """
    #RELATED FIELDS
    oro = models.ForeignKey('Qodex_users', db_column='oro', on_delete=models.SET_NULL, blank=True, null=True)
    #LOCAL FIELDS
    weight_fault = models.IntegerField(blank=True, null=True)
    def __str__(self):
        """ Django-admin UI """
        return self.oro
    class Meta:
        """ Model congigurations """
        managed = True
        db_table = 'Oro_info'