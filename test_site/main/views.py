import json

import requests
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from .models import Article, Code
from datetime import datetime


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
    latest_codes = Code.objects.order_by('-publishing_date')[:10]
    if request.method == "POST":
        shared_code = request.POST.get('share_code', False)
        code = request.POST.get('code', False)
        submit = request.POST.get('submit_code', False)
        # code = request.Post['code']
        if submit and code:
            path = "https://api.jdoodle.com/v1/execute"
            params = {
                "script": code,
                "stdin": "",
                "language": "nodejs",
                "versionIndex": "0",
                "clientId": "eea45300d8deecc52a25aa145b624cdc",
                "clientSecret": "8a188eb5edb8802a1b740a4dc0aceb2dc29439a1d0f3034c9be6ee404cddb6a7"
            }
            response = requests.post(path, headers={"Content-Type": "application/json"}, data=json.dumps(params))
            return render(request, 'main/compile.html',
                          {'output': response.json(), 'user_code': code, 'latest_codes': latest_codes})
        if shared_code and code:
            new_code = Code(code=code, publishing_date = datetime.now())
            new_code.save()
            code = False
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request, 'main/compile.html', {'latest_codes': latest_codes})


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
