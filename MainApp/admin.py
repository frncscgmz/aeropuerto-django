from django.contrib import admin
from Aeropuerto.MainApp.models import Destinos, Reservacion

class DestinosAdmin(admin.ModelAdmin):
	pass
admin.site.register(Destinos,DestinosAdmin)

class ReservacionAdmin(admin.ModelAdmin):
	pass
admin.site.register(Reservacion,ReservacionAdmin)




