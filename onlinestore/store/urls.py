from django.urls import path
from .views import *

urlpatterns = [
    path('main/', MainPage.as_view(), name='main'),
    path('picked-product/<int:category_id>/', PickedProduct.as_view(), name='picked-products'),
    path('product-detail/<int:product_id>/', ProductDetail.as_view(), name='product-detail'),

]
