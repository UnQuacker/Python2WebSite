from main.models import Article
from .serializers import Article_serializer
from rest_framework import viewsets


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = Article_serializer
