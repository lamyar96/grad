from django.contrib import admin
from .models import Organization
from .models import Event

admin.site.register(Organization)
admin.site.register(Event)