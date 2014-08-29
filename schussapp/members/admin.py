from django.contrib import admin
from django import forms
from django.db import models

# Register your models here.
from .models import Member, Pass, Season, MemberType, Price


class MemberAdmin(admin.ModelAdmin):
    formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }

    class Media:
        js = ('ckeditor/ckeditor.js',) # The , at the end of this list IS important.
    
    class Meta:
        model = Member

class PassAdmin(admin.ModelAdmin):
    formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }

    class Media:
        js = ('ckeditor/ckeditor.js',) # The , at the end of this list IS important.
    
    class Meta:
        model = Pass
        
class SeasonAdmin(admin.ModelAdmin):
    formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }

    class Media:
        js = ('ckeditor/ckeditor.js',) # The , at the end of this list IS important.
    
    class Meta:
        model = Season
        
class MemberTypeAdmin(admin.ModelAdmin):
    formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }

    class Media:
        js = ('ckeditor/ckeditor.js',) # The , at the end of this list IS important.
    
    class Meta:
        model = MemberType

class PriceAdmin(admin.ModelAdmin):
    formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }

    class Media:
        js = ('ckeditor/ckeditor.js',) # The , at the end of this list IS important.
    
    class Meta:
        model = Price

admin.site.register(Member, MemberAdmin)
admin.site.register(Pass, PassAdmin)    
admin.site.register(Season, SeasonAdmin)
admin.site.register(MemberType, MemberTypeAdmin)    
admin.site.register(Price, PriceAdmin)
