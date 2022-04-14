import json

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
    api_data = requests.get(
        'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1&sparkline=false').json()
    latest_articles = Article.objects.order_by('-publishing_date')[:10]
    return render(request, 'main/crypto.html', {'latest_articles': latest_articles, 'api_data': api_data})


def compile(request):
    if request.method == "POST":
        path = "https://api.jdoodle.com/v1/execute"
        code = request.POST['code']
        params = {
            "script": code,
            "stdin": "",
            "language": "nodejs",
            "versionIndex": "0",
            "clientId": "eea45300d8deecc52a25aa145b624cdc",
            "clientSecret": "8a188eb5edb8802a1b740a4dc0aceb2dc29439a1d0f3034c9be6ee404cddb6a7"
        }
        response = requests.post(path, headers={"Content-Type": "application/json"}, data=json.dumps(params))
        return render(request, 'main/compile.html', {'output': response.json(), 'user_code':code})
    return render(request, 'main/compile.html')


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
    api_data = requests.get(
        'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1&sparkline=false').json()
    latest_articles = Article.objects.order_by('-publishing_date')[:10]
    return render(request, 'main/cryptoru.html', {'latest_articles': latest_articles, 'api_data': api_data})
