from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import *

from store.models import Category, Product
from store.serializers import CategorySerializer, ProductSerializer


# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = (IsAdminUser,)
    # print(queryset)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = (IsAdminUser,)
