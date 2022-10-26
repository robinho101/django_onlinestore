from django.urls import path
from .views import *

urlpatterns = [
    path('basket/', basket, name='basket'),
    path('product-in-basket-to-model/', product_in_basket_to_model, name='product_in_basket_to_model'),
    path('deletion-the-products-from-model-and-basket/', deletion_the_products_from_model_and_basket,
         name='deletion_the_products_from_model_and_basket'),
    path('toUserSelectionModel/', toUserSelectionModel,
         name='toUserSelectionModel'),
    path('toUserSelection/', toUserSelection,
         name='toUserSelection'),
]
