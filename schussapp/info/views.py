
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib import messages
from django.http import Http404

from datetime import datetime, date

from .models import Article, ArticleGroup
# Create your views here.
### Info index ###
def info_home(request, group=None, article=None):
    context = {'active':'info'}
    page = Article.objects.get(title="Welcome")
    if group and article:
    	group = ' '.join(group.split('-'))
    	title = ' '.join(article.split('-'))
    	print group, article
    	page = get_object_or_404(Article, title=title, article_group__name=group )
    
    context['page'] = page

    #get all top level article groups
    article_groups = ArticleGroup.objects.filter(article_group=None)
    context['article_groups'] = article_groups

    return render(request, 'info/info_home.html', context)