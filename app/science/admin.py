from django.contrib import admin

from .models import Element, SaturationData, State, Storage

# Register your models here.
admin.site.register(Element)
admin.site.register(SaturationData)
admin.site.register(Storage)
admin.site.register(State)
