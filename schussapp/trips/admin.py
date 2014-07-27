from django.contrib import admin

# Register your models here.
from .models import Trip, TripEnrollment


class TripAdmin(admin.ModelAdmin):
    class Meta:
        model = Trip

class TripEnrollmentAdmin(admin.ModelAdmin):
    class Meta:
        model = TripEnrollment

admin.site.register(Trip, TripAdmin)
admin.site.register(TripEnrollment, TripEnrollmentAdmin)  