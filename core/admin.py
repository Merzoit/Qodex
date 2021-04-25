from django.contrib import admin
from core import models

#MODEL REGISTER
admin.site.register(models.Auto)
admin.site.register(models.Auto_model)
admin.site.register(models.Auto_brands)
admin.site.register(models.RFID_ID)
admin.site.register(models.Weight_types)
admin.site.register(models.Trash_cats)
admin.site.register(models.Trash_types)
admin.site.register(models.Qodex_users)
admin.site.register(models.Operators)
admin.site.register(models.Qodex_achive)
admin.site.register(models.Cm_events_log)
admin.site.register(models.Regions)
admin.site.register(models.Oro_info)
admin.site.register(models.RFID_types)

