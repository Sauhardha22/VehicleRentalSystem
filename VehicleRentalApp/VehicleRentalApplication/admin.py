from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Vehicle
# admin.site.register(Vehicle)
admin.site.site_header= 'Vehicle Rental System'
admin.site.index_title= 'Vehicle Rental'
@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['id','name','image','type','cost','description']