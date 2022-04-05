from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'main'

urlpatterns = [
    path('cybersport', views.index),
    path('it', views.it),
    path('cryptocurrency', views.crypto),

    path('cryptocurrency/'+'<int:article_id>', views.detail, name='detailCrypto'),

    path('it/'+'<int:article_id>', views.detail, name='detailIT'),

    path('cybersport/'+'<int:article_id>', views.detail, name='detailCybersport')
]

urlpatterns += staticfiles_urlpatterns()
