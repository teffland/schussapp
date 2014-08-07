from django.contrib import admin
from django import forms
from django.db import models

# Register your models here.
from .models import Article, ArticleGroup


class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }
    fields = ('title', 'article_group', 'author', 'body')
    class Media:
        js = ('ckeditor/ckeditor.js',) # The , at the end of this list IS important.
    
    class Meta:
        model = Article

class ArticleGroupAdmin(admin.ModelAdmin):
    formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }

    class Media:
        js = ('ckeditor/ckeditor.js',) # The , at the end of this list IS important.
    
    class Meta:
        model = ArticleGroup
    
        
admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleGroup, ArticleGroupAdmin)    
