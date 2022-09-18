from django.urls import path
from .views import *

urlpatterns = [
    path('main/', MainPage.as_view(), name='main'),
]
