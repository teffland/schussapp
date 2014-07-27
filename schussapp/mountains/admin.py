from django.contrib import admin

# Register your models here.
from .models import Mountain, MountainCheckin, MountainScheduleSlot


class MountainAdmin(admin.ModelAdmin):
    class Meta:
        model = Mountain

class MountainCheckinAdmin(admin.ModelAdmin):
    class Meta:
        model = MountainCheckin
        
class MountainScheduleSlotAdmin(admin.ModelAdmin):
    class Meta:
        model = MountainScheduleSlot
        
admin.site.register(Mountain, MountainAdmin)
admin.site.register(MountainCheckin, MountainCheckinAdmin)    
admin.site.register(MountainScheduleSlot, MountainScheduleSlotAdmin)