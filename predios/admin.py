from django.contrib import admin
from .models import Predio, Propietario  # importa modelos 

# Se registra el modelo Predio con la clase personalizada PredioAdmin
class PredioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'tipo', 'numero_catastral']

admin.site.register(Predio, PredioAdmin)  # Se reigstra el modelo y su configuración aparecera en la barra


admin.site.register(Propietario)  # Se reigstra el modelo y su configuración aparecera en la barra5555555556005