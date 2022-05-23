import json
import datetime
import requests
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .forms import RegisterUser, LoginForm
from .models import Article, Code
from django.contrib.auth import authenticate, login


def index(request):
    latest_articles = Article.objects.filter(article_type="Cybersport").order_by('-publishing_date')[:10]
    return render(request, 'main/index.html', {'latest_articles': latest_articles})


def it(request):
    latest_articles = Article.objects.filter(article_type="IT").order_by('-publishing_date')[:10]
    return render(request, 'main/it.html', {'latest_articles': latest_articles})


def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("No Page was found!")
    return render(request, "main/detail.html", {'article': a})


def crypto(request):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1&sparkline=false'
    api_data = requests.get(url=url, headers=header).json()
    latest_articles = Article.objects.filter(article_type="Cryptocurrency").order_by('-publishing_date')[:10]
    return render(request, 'main/crypto.html', {'latest_articles': latest_articles, 'api_data': api_data})


def compile(request):
    latest_codes = Code.objects.order_by('-publishing_date')[:10]
    if request.method == "POST":
        shared_code = request.POST.get('share_code', False)
        code = request.POST.get('code', False)
        submit = request.POST.get('submit_code', False)
        language = request.POST.get('language_select', False)
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
    if request.user.is_authenticated:
        return render(request, 'main/profile.html')
    else:
        form = RegisterUser()
        return render(request, 'main/register.html', {'form': form})


def register(request):
    form = RegisterUser()
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request, 'main/profile.html')
    return render(request, 'main/register.html', {'form': form})


def user_login(request):
    message = ""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'main/profile.html')
                else:
                    message = "Disabled account"
            else:
                message = "Invalid login/password"
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form, 'message': message})


def cryptograph(request, cryptocurrency_name):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    url = f'https://api.coingecko.com/api/v3/coins/{cryptocurrency_name}/history?date=20-05-2022&localization=en'
    api_data = requests.get(url=url, headers=header).json()
    api_data = []
    for i in range(7):
        now = datetime.datetime.now() - datetime.timedelta(days=i)
        date = f"{now.day}-{now.month}-{now.year}"
        url = f'https://api.coingecko.com/api/v3/coins/{cryptocurrency_name}/history?date={date}&localization=en'
        api_data.append(requests.get(url=url).json())
    return render(request, 'main/cryptograph.html', {'data': api_data})


# RU

def indexru(request):
    if request.method == 'POST':
        is_register = request.POST.get('register', False)
        if is_register:
            form = RegisterUser(request.POST)
            if form.is_valid():
                form.save(commit=True)
    latest_articles = Article.objects.order_by('-publishing_date')[:10]
    return render(request, 'main/ru/indexru.html', {'latest_articles': latest_articles})


def itru(request):
    latest_articles = Article.objects.order_by('-publishing_date')[:10]
    return render(request, 'main/ru/itru.html', {'latest_articles': latest_articles})


def detailru(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Страница не была найдена!")
    return render(request, "main/ru/detailru.html", {'article': a})


def cryptoru(request):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1&sparkline=false'
    api_data = requests.get(url=url, headers=header).json()
    latest_articles = Article.objects.filter(article_type="Cryptocurrency").order_by('-publishing_date')[:10]
    return render(request, 'main/ru/cryptoru.html', {'latest_articles': latest_articles, 'api_data': api_data})


def compileru(request):
    latest_codes = Code.objects.order_by('-publishing_date')[:10]
    if request.method == "POST":
        shared_code = request.POST.get('share_code', False)
        code = request.POST.get('code', False)
        submit = request.POST.get('submit_code', False)
        language = request.POST.get('language_select', False)
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
            return render(request, 'main/ru/compileru.html',
                          {'output': response.json(), 'user_code': code, 'latest_codes': latest_codes})
        if shared_code and code:
            new_code = Code(code=code, publishing_date=datetime.now())
            new_code.save()
            code = False
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request, 'main/ru/compileru.html', {'latest_codes': latest_codes})


def profileru(request):
    if request.user.is_authenticated:
        return render(request, 'main/ru/profileru.html')
    else:
        form = RegisterUser()
        return render(request, 'main/ru/registerru.html', {'form': form})


def registerru(request):
    form = RegisterUser()
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request, 'main/ru/profileru.html')
    return render(request, 'main/ru/registerru.html', {'form': form})


def user_loginru(request):
    message = ""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'main/ru/profileru.html')
                else:
                    message = "Отключенный Аккаунт"
            else:
                message = "Неправильный логин/пароль"
    else:
        form = LoginForm()
    return render(request, 'main/ru/loginru.html', {'form': form, 'message': message})


def cryptographru(request, cryptocurrency_name):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    url = f'https://api.coingecko.com/api/v3/coins/{cryptocurrency_name}/history?date=20-05-2022&localization=en'
    api_data = requests.get(url=url, headers=header).json()
    api_data = []
    for i in range(7):
        now = datetime.datetime.now() - datetime.timedelta(days=i)
        date = f"{now.day}-{now.month}-{now.year}"
        url = f'https://api.coingecko.com/api/v3/coins/{cryptocurrency_name}/history?date={date}&localization=en'
        api_data.append(requests.get(url=url).json())
    return render(request, 'main/ru/cryptographru.html', {'data': api_data})
