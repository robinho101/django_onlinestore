import json
from django.db.models import *
from django.core.paginator import *
from django.core.cache import cache
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


# def search_filter_or_sort_by(request, value, category_id, obj_of_filters):
#     if value == 'sort_by':
#         Product.objects.create(user=request.user, category_id=Product.objects.latest('created_at').category_id,
#                                title=Product.objects.latest('created_at').title,
#                                manufacturer=Product.objects.latest('created_at').manufacturer,
#                                description=Product.objects.latest('created_at').description,
#                                image=Product.objects.latest('created_at').image,
#                                price=Product.objects.latest('created_at').price, sort_by=obj_of_filters[value],
#                                ram=Product.objects.latest('created_at').ram,
#                                processor=Product.objects.latest('created_at').processor,
#                                vram=Product.objects.latest('created_at').vram,
#                                hdd_type=Product.objects.latest('created_at').hdd_type,
#                                tyre_section_width=Product.objects.latest('created_at').tyre_section_width,
#                                tyre_section_height=Product.objects.latest('created_at').tyre_section_height,
#                                season=Product.objects.latest('created_at').season,
#                                diameter=Product.objects.latest('created_at').diameter)
#         Product.objects.all().order_by('-id')[1].delete()
#     elif value:
#         Product.objects.create(user=request.user, category_id=Product.objects.latest('created_at').category_id,
#                                title=Product.objects.latest('created_at').title,
#                                manufacturer=Product.objects.latest('created_at').manufacturer,
#                                description=Product.objects.latest('created_at').description,
#                                image=Product.objects.latest('created_at').image,
#                                price=Product.objects.latest('created_at').price,
#                                ram=Product.objects.latest('created_at').ram,
#                                processor=Product.objects.latest('created_at').processor,
#                                vram=Product.objects.latest('created_at').vram,
#                                hdd_type=Product.objects.latest('created_at').hdd_type,
#                                tyre_section_width=Product.objects.latest('created_at').tyre_section_width,
#                                tyre_section_height=Product.objects.latest('created_at').tyre_section_height,
#                                season=Product.objects.latest('created_at').season,
#                                diameter=Product.objects.latest('created_at').diameter,
#                                search_filter=value)
#         Product.objects.all().order_by('-id')[1].delete()


def unique_values(request, category_id):
    all_values = []
    unique_values_list = []

    if category_id == 1:
        for item in Product.objects.filter(category_id=category_id):
            if 'manufacturer' + item.manufacturer not in all_values:
                all_values.append('manufacturer' + item.manufacturer)
                unique_values_list.append({'manufacturer': item.manufacturer})
            if 'ram' + item.ram not in all_values:
                all_values.append('ram' + item.ram)
                unique_values_list.append({'ram': item.ram})
            if 'vram' + item.vram not in all_values:
                all_values.append('vram' + item.vram)
                unique_values_list.append({'vram': item.vram})
            if 'processor' + item.processor not in all_values:
                all_values.append('processor' + item.processor)
                unique_values_list.append({'processor': item.processor})
            if 'hdd_type' + item.hdd_type not in all_values:
                all_values.append('hdd_type' + item.hdd_type)
                unique_values_list.append({'hdd_type': item.hdd_type})
    elif category_id == 2:
        for item in Product.objects.filter(category_id=category_id):
            if item.manufacturer not in all_values:
                all_values.append(item.manufacturer)
                unique_values_list.append({'manufacturer': item.manufacturer})
            if item.tyre_section_width not in all_values:
                all_values.append(item.tyre_section_width)
                unique_values_list.append({'ram': item.tyre_section_width})
            if item.tyre_section_height not in all_values:
                all_values.append(item.tyre_section_height)
                unique_values_list.append({'vram': item.tyre_section_height})
            if item.season not in all_values:
                all_values.append(item.season)
                unique_values_list.append({'processor': item.season})
            if item.diameter not in all_values:
                all_values.append(item.diameter)
                unique_values_list.append({'hdd_type': item.diameter})
    return unique_values_list


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
        'title': Category.objects.get(pk=category_id),
        'category_id': category_id,
        'min': Product.objects.filter(category_id=category_id).aggregate(Min('price')),
        'max': Product.objects.filter(category_id=category_id).aggregate(Max('price')),
        'filters_object': unique_values(request, category_id)
    }

    if request.body:
        py_dict = json.loads(request.body)
        if 'search_filter' in py_dict:
            cache.set('search_filter_or_sort_by', py_dict, 10)
            # search_filter_or_sort_by(request, True, category_id, py_dict)
        if 'sort_by' in py_dict:
            cache.set('search_filter_or_sort_by', {'sort_by': py_dict['sort_by']}, 10)

    search_filter_or_sort_by = cache.get('search_filter_or_sort_by')

    # search_filter_or_sort_by(request, 'sort_by', 'not', py_dict)
    # Product.objects.create(user=request.user, category_id=Product.objects.latest('created_at').category_id,
    #                        title=Product.objects.latest('created_at').title,
    #                        manufacturer=Product.objects.latest('created_at').manufacturer,
    #                        description=Product.objects.latest('created_at').description,
    #                        image=Product.objects.latest('created_at').image,
    #                        price=Product.objects.latest('created_at').price, sort_by=py_dict['sort_by'],
    #                        ram=Product.objects.latest('created_at').ram,
    #                        processor=Product.objects.latest('created_at').processor,
    #                        vram=Product.objects.latest('created_at').vram,
    #                        hdd_type=Product.objects.latest('created_at').hdd_type,
    #                        tyre_section_width=Product.objects.latest('created_at').tyre_section_width,
    #                        tyre_section_height=Product.objects.latest('created_at').tyre_section_height,
    #                        season=Product.objects.latest('created_at').season,
    #                        diameter=Product.objects.latest('created_at').diameter)
    # Product.objects.all().order_by('-id')[1].delete()

    if search_filter_or_sort_by:
        if 'sort_by' in search_filter_or_sort_by:
            pickedProductList = Product.objects.filter(category_id=category_id).order_by(
                search_filter_or_sort_by['sort_by'] + 'price')
            context['page_obj'] = get_paginate(request, pickedProductList, 5)
            return render(request, 'store/picked-product.html', context=context)

        if 'search_filter' in search_filter_or_sort_by and category_id == 1:
            pickedProductList = Product.objects.filter(category_id=category_id,
                                                       price__gte=search_filter_or_sort_by['priceMin'],
                                                       price__lte=search_filter_or_sort_by['priceMax'],
                                                       **search_filter_or_sort_by['other_filters'])

            context['page_obj'] = get_paginate(request, pickedProductList, 5)
            return render(request, 'store/picked-product.html', context=context)

        elif 'search_filter' in search_filter_or_sort_by and category_id == 2:
            pickedProductList = Product.objects.filter(category_id=category_id,
                                                       price__gte=search_filter_or_sort_by['priceMin'],
                                                       price__lte=search_filter_or_sort_by['priceMax'],
                                                       **search_filter_or_sort_by['other_filters'])

            context['page_obj'] = get_paginate(request, pickedProductList, 5)
            return render(request, 'store/picked-product.html', context=context)

    pickedProductList = Product.objects.filter(category_id=category_id)
    context['page_obj'] = get_paginate(request, pickedProductList, 5)
    return render(request, 'store/picked-product.html', context=context)


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
    viewed_items_list = []
    if len(viewed_items_list) <= 9:
        viewed_items_list = ViewedItems.objects.filter(user=request.user).order_by('-number')
    else:
        viewed_items_list = ViewedItems.objects.filter(user=request.user).order_by('-number')[:10]
    for item in viewed_items_list:
        item.pkNum = Product.objects.get(user=request.user, title=item.title).pk

    return viewed_items_list
