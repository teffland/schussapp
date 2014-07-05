from django.contrib import admin

# Register your models here.
from .models import Member, Pass, Season


class MemberAdmin(admin.ModelAdmin):
    class Meta:
        model = Member

class PassAdmin(admin.ModelAdmin):
    class Meta:
        model = Pass
        
class SeasonAdmin(admin.ModelAdmin):
    class Meta:
        model = Season
        
admin.site.register(Member, MemberAdmin)
admin.site.register(Pass, PassAdmin)    
admin.site.register(Season, SeasonAdmin)