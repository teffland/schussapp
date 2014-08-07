from django.shortcuts import render

from .models import Article, ArticleGroup
# Create your views here.
### Info index ###
def info_home(request):
    context = {'active':'info'}
    article = Article.objects.all()[0]
    context['a'] = article
    article_groups = ArticleGroup.objects.all()
    context['article_groups'] = article_groups

    return render(request, 'info/info_home.html', context)