from django.urls import path, include
from django.urls import path, include, re_path
from rest_framework import routers
from api.views import *

router_category = routers.DefaultRouter()
router_category.register(r'category', CategoryViewSet)

router_product = routers.DefaultRouter()
router_product.register(r'product', ProductViewSet)

urlpatterns = [
    path('api-drf-auth/', include('rest_framework.urls')),
    path('category-api-entry/', include(router_category.urls)),
    path('product-api-entry/', include(router_product.urls)),
    path('api-auth/', include('djoser.urls')),
    re_path('auth/', include('djoser.urls.authtoken')),  # http://127.0.0.1:8000/auth/token/login
]
