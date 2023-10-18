from django.contrib import admin

from .models import Element, SaturationData, Storage

# Register your models here.
admin.site.register(Element)
admin.site.register(SaturationData)
admin.site.register(Storage)
