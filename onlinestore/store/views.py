import json

from django.core.paginator import *
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView, DetailView, CreateView
from store.models import *


# Create your views here.

def get_paginate(request, obj, num_of_elem):
    paginator = Paginator(obj, num_of_elem)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    return page_objects


def searchResult(request):
    if request.body:
        py_dict = json.loads(request.body)
        if 'sort_by' in py_dict:
            if py_dict['sort_by']:
                if SearchQuery.objects.latest('created_at').category:
                    SearchQuery.objects.create(category=SearchQuery.objects.latest('created_at').category,
                                               description=SearchQuery.objects.latest('created_at').description,
                                               sort_by=py_dict['sort_by'])
                    return JsonResponse('', safe=False)
                else:
                    SearchQuery.objects.create(category=SearchQuery.objects.latest('created_at').category,
                                               description=SearchQuery.objects.latest('created_at').description,
                                               sort_by=py_dict['sort_by'])
                    return JsonResponse('', safe=False)
            else:
                if SearchQuery.objects.latest('created_at').category:
                    SearchQuery.objects.create(category=SearchQuery.objects.latest('created_at').category,
                                               description=SearchQuery.objects.latest('created_at').description,
                                               sort_by=py_dict['sort_by'])
                    return JsonResponse('', safe=False)
                else:
                    SearchQuery.objects.create(category=SearchQuery.objects.latest('created_at').category,
                                               description=SearchQuery.objects.latest('created_at').description,
                                               sort_by=py_dict['sort_by'])
                    return JsonResponse('', safe=False)

        else:
            SearchQuery.objects.create(category=py_dict['selectedCategoryId'], description=py_dict['text'])
            return JsonResponse('', safe=False)

    elif SearchQuery.objects.latest('created_at').category:
        if not SearchQuery.objects.latest('created_at').sort_by:
            search_list = Product.objects.filter(category=SearchQuery.objects.latest('created_at').category,
                                                 description__icontains=SearchQuery.objects.latest(
                                                     'created_at').description).order_by('price')

            context = {
                'page_obj': get_paginate(request, search_list, 5)
            }
            return render(request, 'store/searchResult.html', context=context)
        else:
            search_list = Product.objects.filter(category=SearchQuery.objects.latest('created_at').category,
                                                 description__icontains=SearchQuery.objects.latest(
                                                     'created_at').description).order_by('-price')

            context = {
                'page_obj': get_paginate(request, search_list, 5)
            }
            return render(request, 'store/searchResult.html', context=context)

    else:
        if not SearchQuery.objects.latest('created_at').sort_by:
            search_list = Product.objects.filter(
                description__icontains=SearchQuery.objects.latest('created_at').description).order_by('price')

            context = {
                'page_obj': get_paginate(request, search_list, 5)
            }
            return render(request, 'store/searchResult.html', context=context)
        else:
            search_list = Product.objects.filter(
                description__icontains=SearchQuery.objects.latest('created_at').description).order_by('-price')

            context = {
                'page_obj': get_paginate(request, search_list, 5)
            }
            return render(request, 'store/searchResult.html', context=context)


class MainPage(ListView):
    model = Category
    template_name = 'store/main_page.html'
    context_object_name = 'category'


def pickedProduct(request, category_id):
    context = {
        'title': Category.objects.get(pk=category_id)
    }
    if request.body:
        py_dict = json.loads(request.body)
        if 'sort_by' in py_dict:
            Product.objects.create(user=request.user, category_id=category_id,
                                   title=Product.objects.latest('created_at').title,
                                   manufacturer=Product.objects.latest('created_at').manufacturer,
                                   description=Product.objects.latest('created_at').description,
                                   image=Product.objects.latest('created_at').image,
                                   price=Product.objects.latest('created_at').price, sort_by=py_dict['sort_by'])
            Product.objects.filter(id=Product.objects.latest('id').id - 1).delete()

    if Product.objects.latest('created_at').sort_by == 'not':
        pickedProductList = Product.objects.filter(category_id=category_id)
        context['page_obj'] = get_paginate(request, pickedProductList, 5)
        return render(request, 'store/picked-product.html', context=context)
    elif Product.objects.latest('created_at').sort_by == '-':
        pickedProductList = Product.objects.filter(category_id=category_id).order_by('-price')
        context['page_obj'] = get_paginate(request, pickedProductList, 5)
        return render(request, 'store/picked-product.html', context=context)
    else:
        pickedProductList = Product.objects.filter(category_id=category_id).order_by('price')
        context['page_obj'] = get_paginate(request, pickedProductList, 5)
        return render(request, 'store/picked-product.html', context=context)


# class PickedProduct(ListView):
#     model = Product
#     template_name = 'store/picked-product.html'
#     context_object_name = 'product'
#     paginate_by = 5
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super(PickedProduct, self).get_context_data(**kwargs)
#         context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
#         return context
#
#     def get_queryset(self):
#         if self.request.body:
#             py_dict = json.loads(self.request.body)
#             if 'sort_by' in py_dict:
#                 Product.objects.create(category_id=self.kwargs['category_id'],
#                                        title=Product.objects.latest('created_at').title,
#                                        manufacturer=Product.objects.latest('created_at').manufacturer,
#                                        description=Product.objects.latest('created_at').description,
#                                        image=Product.objects.latest('created_at').image,
#                                        price=Product.objects.latest('created_at').price, sort_by=py_dict['sort_by'])
#                 Product.objects.filter(id=Product.objects.latest('id').id - 1).delete()
#
#         if Product.objects.latest('created_at').sort_by == 'not':
#             return Product.objects.filter(category_id=self.kwargs['category_id'])
#         elif Product.objects.latest('created_at').sort_by == '-':
#             return Product.objects.filter(category_id=self.kwargs['category_id']).order_by('-price')
#         else:
#             return Product.objects.filter(category_id=self.kwargs['category_id']).order_by('price')


class ProductDetail(ListView):
    model = Product
    template_name = 'store/product-detail.html'
    context_object_name = 'productDetail'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        context['productList'] = Product.objects.filter(
            category_id=Product.objects.get(pk=self.kwargs['product_id']).category_id)
        context['viewed_items_list'] = mostViewed(self.request)
        return context

    def get_queryset(self):
        return Product.objects.filter(pk=self.kwargs['product_id'])


def toViewedItemsModel(request):
    py_dict = json.loads(request.body)

    if ViewedItems.objects.filter(user=request.user, title=py_dict['title']):
        changing_field = ViewedItems.objects.get(user=request.user, title=py_dict['title'])
        changing_field.number += 1
        changing_field.save()
    else:
        ViewedItems.objects.create(user=request.user, title=py_dict['title'], description=py_dict['description'],
                                   price=py_dict['price'], image=py_dict['image'])

    return JsonResponse('empty)', safe=False)


def mostViewed(request):
    viewed_items_list = ViewedItems.objects.filter(user=request.user).order_by('-number')[:10]
    for item in viewed_items_list:
        item.pkNum = Product.objects.get(user=request.user, title=item.title).pk

    return viewed_items_list
