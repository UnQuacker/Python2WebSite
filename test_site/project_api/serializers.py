from rest_framework import serializers
# from test_site.main import models
# from test_site.main.models import Article
# from test_site.main.models import *
from main.models import Article


class Article_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
