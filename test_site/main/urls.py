from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'main'

urlpatterns = [
    # EN

    path('en/cybersport', views.index, name='cybersport'),
    path('en/it', views.it, name='it'),
    path('en/cryptocurrency', views.crypto, name='cryptocurrency'),

    path('en/cryptocurrency/' + '<int:article_id>', views.detail, name='detailCrypto'),

    path('en/cryptocurrency/graph/' + '<str:cryptocurrency_name>', views.cryptograph, name='cryptoGraph'),

    path('en/it/' + '<int:article_id>', views.detail, name='detailIT'),

    path('en/cybersport/' + '<int:article_id>', views.detail, name='detailCybersport'),

    path('en/coding', views.compile, name='compile'),

    path('en/profile', views.profile, name='profile'),

    path('en/login', views.user_login, name='login'),

    path('en/register', views.register, name='register'),
    # RU

    path('ru/cybersport', views.indexru),
    path('ru/it', views.itru),
    path('ru/cryptocurrency', views.cryptoru),

    path('ru/cryptocurrency/' + '<int:article_id>', views.detailru, name='detailCryptoRu'),

    path('ru/it/' + '<int:article_id>', views.detailru, name='detailITRu'),

    path('ru/cybersport/' + '<int:article_id>', views.detailru, name='detailCybersportRu'),

    path('ru/coding', views.compileru, name='compileRu'),

]

urlpatterns += staticfiles_urlpatterns()
