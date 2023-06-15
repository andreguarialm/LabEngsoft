from django.contrib import admin
from .models import Voo
from .forms import VooForm

@admin.register(Voo)
class VooAdmin(admin.ModelAdmin):
    form = VooForm
    

