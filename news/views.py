from django.shortcuts import render,get_object_or_404
from .models import News
from django.core.paginator import Paginator


def news_list_view(request):

    title = ''
    news = News.objects.all()

    if request.LANGUAGE_CODE == 'de':
        title = 'Haberler - ARSLANYAPI'
    else:
        title = 'News - ARSLANYAPI'

    paginator = Paginator(news,12) #

    page = request.GET.get('sayfa')
    news_page = paginator.get_page(page)

    context = {
        'title':title,
        'all_objects':news_page,
    }

    return render(request,'news/news-list.html',context)


def news_detail_view(request,slug):

    news = get_object_or_404(News, slug=slug)
    last_news = News.objects.all()[0:3]

    all_news = News.objects.all()

    index = 0

    previous_news = None
    next_news = None

    for x in all_news:

        if x.id != news.id:

            index +=1
        else:
            break

    if index >= 0 and index < len(all_news):
        previous_news = News.objects.all()[index+1:index+2]

    if index <= len(all_news) and index > 0:
        next_news =  News.objects.all()[index-1:index]

    if request.LANGUAGE_CODE == 'de':
        title = news.title_de
    else:
        title = news.title_en

    context = {
        'title':title,
        'news':news,
        'last_news':last_news,
        'previous_news':previous_news,
        'next_news':next_news,
    }

    return render(request,'news/news-detail.html',context)
