from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('api_test', api_test)

]
