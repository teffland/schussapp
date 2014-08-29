from django.db import models

from datetime import datetime, date
# Create your models here.

"""
 * Article:
 *  Written entry to info section on how to do stuff
 *
 * Fields:
 *   Author, article group, created, modified, published
"""
class Article(models.Model):
    
    title = models.CharField(max_length=40)
    author = models.CharField(max_length=50)
    #articles share named groups (like chapters)
    article_group = models.ForeignKey('ArticleGroup')

    body = models.TextField()
    #Allow an article to be the child of another
    #parent_article = models.ForeignKey('Article', blank=True, null=True)
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    is_published = models.BooleanField()

    def __unicode__(self):
        return self.title + ' (' + unicode(self.article_group)+ ')'

class ArticleGroup(models.Model):
    name = models.CharField(max_length=100)

    article_group = models.ForeignKey('ArticleGroup', blank=True, null=True)

    description = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def articles(self):
        articles = Article.objects.filter(article_group=self)
        return articles

    def subgroups(self):
        subgroups = ArticleGroup.objects.filter(article_group=self)
        return subgroups

    def __unicode__(self):
        return self.name

