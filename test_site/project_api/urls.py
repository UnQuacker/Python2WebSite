from django.urls import path, include
from . import views
from .views import *
from .router import router
from rest_framework.authtoken import views

urlpatterns = [
    path('api_test', api_test),
    path('router_test/', include(router.urls)),
    path('api-token-auth', views.obtain_auth_token, name='api-token-auth')
]
