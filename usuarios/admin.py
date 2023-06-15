from django.contrib import admin
from .models import Socio, CertificadoIntrutor

# Register your models here.
# admin.site.register(Socio)
admin.site.register(CertificadoIntrutor)

@admin.register(Socio)
class SocioAdmin(admin.ModelAdmin):
    list_display = ("id", "__str__")
    