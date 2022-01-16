from simpleAPI.models import UUID
from django.contrib import admin

class UUIDAdmin(admin.ModelAdmin):
      list_display    = ['created', 'uuid']

admin.site.register(UUID, UUIDAdmin)