from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.
class DatosAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','descripcion']
    search_fields = ['id']
    list_per_page = 1


admin.site.register(Datos, DatosAdmin)