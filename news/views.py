from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import News

def news(request):
    paginator = Paginator(News.objects.all().filter(published=True).order_by('-created'), 25)
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        news = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        news = paginator.page(paginator.num_pages)
    return render(request, 'news/index.html', {'news': news})

def the_news(request, slug):
    the_news = get_object_or_404(News, slug=slug)
    return render(request, 'news/the_news.html', {'the_news': the_news,})
