from django.urls import path
from .views import *


urlpatterns = [
    path('', greeting),
    path('spanish', spanish_greeting),
    path('chinese', chinese_greeting),
]
