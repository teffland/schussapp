from django.contrib import admin

# Register your models here.
from .models import Bus, BusCheckin


class BusAdmin(admin.ModelAdmin):
    class Meta:
        model = Bus

class BusCheckinAdmin(admin.ModelAdmin):
    class Meta:
        model = BusCheckin

admin.site.register(Bus, BusAdmin)
admin.site.register(BusCheckin, BusCheckinAdmin)    
