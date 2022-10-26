from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.core.paginator import *
from store.models import *
from django.views.generic import ListView, DetailView, CreateView


# Create your views here.

class MainPage(ListView):
    model = Category
    template_name = 'store/main_page.html'
    context_object_name = 'category'


class PickedProduct(ListView):
    model = Product
    template_name = 'store/picked-product.html'
    context_object_name = 'product'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PickedProduct, self).get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return Product.objects.filter(category_id=self.kwargs['category_id'])


class ProductDetail(ListView):
    model = Product
    template_name = 'store/product-detail.html'
    context_object_name = 'productDetail'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        context['productList'] = Product.objects.filter(
            category_id=Product.objects.get(pk=self.kwargs['product_id']).category_id)

        return context

    def get_queryset(self):
        return Product.objects.filter(pk=self.kwargs['product_id'])
