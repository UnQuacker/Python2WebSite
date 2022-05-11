import json

import requests
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterUser, LoginForm
from .models import Article, Code
from datetime import datetime
from django.contrib.auth import authenticate, login


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
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # return HttpResponse('Authenticated successfully')
                    return render(request, 'main/profile.html')
                else:
                    message = "Disabled account"
            else:
                message = "Invalid login/password"
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form, 'message': message})


# def return_form(request):
#     form = RegisterUser()
#     if request.method == 'POST':
#         # is_register = request.POST.get('register', False)
#         # if is_register:
#         form = RegisterUser(request.POST)
#         if form.is_valid():
#             form.save(commit=True)
#         # else:
#         #     messages.error(request, 'not valid')
#     # else:
#     #     messages.error(request, '!registered' + str(request.POST.get('register')))
#     # else:
#     #     messages.error(request, 'not post')
    return form


def register(request):
    form = RegisterUser()
    if request.method == 'POST':
        # is_register = request.POST.get('register', False)
        # if is_register:
        form = RegisterUser(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request, 'main/profile.html')
        # else:
        #     messages.error(request, 'not valid')
    # else:
    #     messages.error(request, '!registered' + str(request.POST.get('register')))
    # else:
    #     messages.error(request, 'not post')
    return render(request, 'main/register.html', {'form': form})


# def return_language_form(request):
#     form = LanguageForm(request.POST)
#     if form.is_valid():
#         form.save(coomit=True)
#     return form


def index(request):
    # form = return_form(request)
    # form = RegisterUser()
    # if request.method == 'POST':
    #     is_register = request.POST.get('register', False)
    #     if is_register:
    #         form = RegisterUser(request.POST)
    #         if form.is_valid():
    #             form.save(commit=True)
    latest_articles = Article.objects.filter(article_type="Cybersport").order_by('-publishing_date')[:10]
    return render(request, 'main/index.html', {'latest_articles': latest_articles})


def it(request):
    # form = return_form(request)
    latest_articles = Article.objects.filter(article_type="IT").order_by('-publishing_date')[:10]
    return render(request, 'main/it.html', {'latest_articles': latest_articles})


def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("No Page was found!")
    # form = return_form(request)
    return render(request, "main/detail.html", {'article': a})


def crypto(request):
    # form = return_form(request)
    api_data = requests.get(
        'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1&sparkline=false').json()
    latest_articles = Article.objects.filter(article_type="Cryptocurrency").order_by('-publishing_date')[:10]
    return render(request, 'main/crypto.html', {'latest_articles': latest_articles, 'api_data': api_data})


def compile(request):
    # if request.user.is_authenticated:
    #     test1 = request.user.username
    # else:
    #     test1 = "not authenticated"
    # form = return_form(request)
    latest_codes = Code.objects.order_by('-publishing_date')[:10]
    if request.method == "POST":
        shared_code = request.POST.get('share_code', False)
        code = request.POST.get('code', False)
        submit = request.POST.get('submit_code', False)
        # code = request.Post['code']
        language = request.POST.get('language_select', False)
        # language2 = request.POST.get('nodejs', False)
        # language3 = request.POST.get('python', False)
        # language4 = request.POST.get('java', False)
        if submit and code:
            path = "https://api.jdoodle.com/v1/execute"
            params = {
                "script": code,
                "stdin": "",
                "language": language,
                "versionIndex": "0",
                "clientId": "eea45300d8deecc52a25aa145b624cdc",
                "clientSecret": "8a188eb5edb8802a1b740a4dc0aceb2dc29439a1d0f3034c9be6ee404cddb6a7"
            }
            response = requests.post(path, headers={"Content-Type": "application/json"}, data=json.dumps(params))
            return render(request, 'main/compile.html',
                          {'output': response.json(), 'user_code': code, 'latest_codes': latest_codes})
        if shared_code and code:
            new_code = Code(code=code, publishing_date=datetime.now())
            new_code.save()
            code = False
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request, 'main/compile.html', {'latest_codes': latest_codes})


def profile(request):
    return render(request, 'main/profile.html')


# def loginView(request):
#     return render(request, 'main/login.html')


# def registerView(request):
#     return render(request, 'main/register.html')


# RU

def indexru(request):
    # form = RegisterUser()
    if request.method == 'POST':
        is_register = request.POST.get('register', False)
        if is_register:
            form = RegisterUser(request.POST)
            if form.is_valid():
                form.save(commit=True)
    latest_articles = Article.objects.order_by('-publishing_date')[:10]
    return render(request, 'main/ru/indexru.html', {'latest_articles': latest_articles})


def itru(request):
    # form = return_form(request)
    latest_articles = Article.objects.order_by('-publishing_date')[:10]
    return render(request, 'main/ru/itru.html', {'latest_articles': latest_articles})


def detailru(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Страница не была найдена!")
    # form = return_form(request)
    return render(request, "main/ru/detailru.html", {'article': a})


def cryptoru(request):
    # form = return_form(request)
    api_data = requests.get(
        'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1&sparkline=false').json()
    latest_articles = Article.objects.order_by('-publishing_date')[:10]
    return render(request, 'main/ru/cryptoru.html',
                  {'latest_articles': latest_articles, 'api_data': api_data})


def compileru(request):
    # if request.user.is_authenticated:
    #     test1 = request.user.username
    # else:
    #     test1 = "not authenticated"
    # form = return_form(request)
    latest_codes = Code.objects.order_by('-publishing_date')[:10]
    if request.method == "POST":
        shared_code = request.POST.get('share_code', False)
        code = request.POST.get('code', False)
        submit = request.POST.get('submit_code', False)
        # code = request.Post['code']
        language = request.POST.get('language_select', False)
        # language2 = request.POST.get('nodejs', False)
        # language3 = request.POST.get('python', False)
        # language4 = request.POST.get('java', False)
        if submit and code:
            path = "https://api.jdoodle.com/v1/execute"
            params = {
                "script": code,
                "stdin": "",
                "language": language,
                "versionIndex": "0",
                "clientId": "eea45300d8deecc52a25aa145b624cdc",
                "clientSecret": "8a188eb5edb8802a1b740a4dc0aceb2dc29439a1d0f3034c9be6ee404cddb6a7"
            }
            response = requests.post(path, headers={"Content-Type": "application/json"}, data=json.dumps(params))
            return render(request, 'main/ru/compile.html',
                          {'output': response.json(), 'user_code': code, 'latest_codes': latest_codes})
        if shared_code and code:
            new_code = Code(code=code, publishing_date=datetime.now())
            new_code.save()
            code = False
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request, 'main/ru/compile.html', {'latest_codes': latest_codes})
