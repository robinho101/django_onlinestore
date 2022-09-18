from django.shortcuts import render
from store.models import *
from django.views.generic import ListView, DetailView, CreateView


# Create your views here.

class MainPage(ListView):
    model = Category
    template_name = 'store/main_page.html'
    context_object_name = 'category'
