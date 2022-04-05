from django.db import models


class Article(models.Model):
    article_type = models.CharField('article type', max_length=50)
    article_title = models.CharField('article name', max_length=200)
    article_text = models.TextField('article text')
    publishing_date = models.DateTimeField('publishing date')


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment_author = models.CharField('comment author', max_length=100)
    comment_text = models.TextField('comment text')