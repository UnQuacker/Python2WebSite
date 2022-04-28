import json

import requests
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterUser
from .models import Article, Code
from datetime import datetime


# EN
# def register(request):
#     form = RegisterUser()
#     if request.method == 'POST':
#         register = request.POST.get('register', False)
#         if register:
#             form = RegisterUser(request.POST)
#             if form.is_valid():
#                 form.save()
#             else:
#                 return render(request, 'main/base.html', status=204)
#
#     return render(request, 'main/base.html', status=204)


def return_form(request):
    form = RegisterUser()
    if request.method == 'POST':
        # is_register = request.POST.get('register', False)
        # if is_register:
            form = RegisterUser(request.POST)
            if form.is_valid():
                form.save(commit=True)
            # else:
            #     messages.error(request, 'not valid')
        # else:
        #     messages.error(request, '!registered' + str(request.POST.get('register')))
    # else:
    #     messages.error(request, 'not post')
    return form


def index(request):
    form = RegisterUser()
    if request.method == 'POST':
        is_register = request.POST.get('register', False)
        if is_register:
            form = RegisterUser(request.POST)
            if form.is_valid():
                form.save(commit=True)
    latest_articles = Article.objects.order_by('-publishing_date')[:10]
    return render(request, 'main/index.html', {'latest_articles': latest_articles, 'form': form})


def it(request):
    form = return_form(request)
    latest_articles = Article.objects.order_by('-publishing_date')[:10]
    return render(request, 'main/it.html', {'latest_articles': latest_articles, 'form': form})


def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("No Page was found!")
    form = return_form(request)
    return render(request, "main/detail.html", {'article': a, 'form': form})


def crypto(request):
    form = return_form(request)
    api_data = requests.get(
        'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1&sparkline=false').json()
    latest_articles = Article.objects.order_by('-publishing_date')[:10]
    return render(request, 'main/crypto.html', {'latest_articles': latest_articles, 'api_data': api_data, 'form': form})


def compile(request):
    form = return_form(request)
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
                          {'output': response.json(), 'user_code': code, 'latest_codes': latest_codes, 'form': form})
        if shared_code and code:
            new_code = Code(code=code, publishing_date=datetime.now())
            new_code.save()
            code = False
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request, 'main/compile.html', {'latest_codes': latest_codes, 'form': form})


def profile(request):
    return render(request, 'main/profile.html')


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
