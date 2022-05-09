# from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from main.models import *
from rest_framework.parsers import JSONParser

from .serializers import *


# class API_test(generics.ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = Article_serializer
# Create your views here.

@csrf_exempt
def api_test(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = Article_serializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Article_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201, safe=False)
        return JsonResponse(serializer.errors, status=400)
