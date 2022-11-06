from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('main/', MainPage.as_view(), name='main'),
    path('picked-product/<int:category_id>/', pickedProduct, name='picked-products'),
    path('product-detail/<int:product_id>/', ProductDetail.as_view(), name='product-detail'),
    path('to-viewed-items-model/', toViewedItemsModel, name='to-viewed-items-model'),
    path('search-result/', searchResult, name='search-result'),
]
