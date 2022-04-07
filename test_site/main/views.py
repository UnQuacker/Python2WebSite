import requests
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Article


# EN


def index(request):
    latest_articles = Article.objects.order_by('-publishing_date')[:10]
    return render(request, 'main/index.html', {'latest_articles': latest_articles})


def it(request):
    latest_articles = Article.objects.order_by('-publishing_date')[:10]
    return render(request, 'main/it.html', {'latest_articles': latest_articles})


def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("No Page was found!")
    return render(request, "main/detail.html", {'article': a})


def crypto(request):
    api_data = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1&sparkline=false').json()
    latest_articles = Article.objects.order_by('-publishing_date')[:10]
    return render(request, 'main/crypto.html', {'latest_articles': latest_articles, 'api_data':api_data})

# RU

def indexru(request):
    latest_articles = Article.objects.order_by('-publishing_date')[:10]
    return render(request, 'main/indexru.html', {'latest_articles': latest_articles})


def itru(request):
    latest_articles = Article.objects.order_by('-publishing_date')[:10]
    return render(request, 'main/itru.html', {'latest_articles': latest_articles})


def detailru(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Страница не найдена!")
    return render(request, "main/detailru.html", {'article': a})


def cryptoru(request):
    api_data = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1&sparkline=false').json()
    latest_articles = Article.objects.order_by('-publishing_date')[:10]
    return render(request, 'main/cryptoru.html', {'latest_articles': latest_articles, 'api_data':api_data})