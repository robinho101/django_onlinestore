import json
from cloudipsp import Api, Checkout
from django.core.paginator import *
from django.db.models import *
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.core.cache import cache
from django.views.generic import ListView, DetailView, CreateView
from store.models import *
from .models import *
from store.views import mostViewed
from store.views import get_paginate


# Create your views here.
def toPurchasedItemsModel(request):
    py_dict = json.loads(request.body)
    PurchasedItemsModel.objects.create(user=request.user, order_id=py_dict['order_id'], image=py_dict['image'],
                                       title=py_dict['title'], price=py_dict['price'], amount=py_dict['amount'])

    return HttpResponse('')


def purchasedItems(request):
    try:
        context = {}
        if request.body:
            py_dict = json.loads(request.body)
            if 'sort_by' in py_dict:
                PurchasedItemsModel.objects.create(user=request.user,
                                                   order_id=PurchasedItemsModel.objects.latest('created_at').order_id,
                                                   image=PurchasedItemsModel.objects.latest('created_at').image,
                                                   title=PurchasedItemsModel.objects.latest('created_at').title,
                                                   price=PurchasedItemsModel.objects.latest('created_at').price,
                                                   amount=PurchasedItemsModel.objects.latest('created_at').amount,
                                                   sort_by=py_dict['sort_by'])
                PurchasedItemsModel.objects.filter(id=PurchasedItemsModel.objects.latest('id').id - 1).delete()

        if PurchasedItemsModel.objects.latest('created_at').sort_by == 'not':
            purchasedItemsList = PurchasedItemsModel.objects.filter(user=request.user)
            items = purchasedItemsList
            for item in items:
                item.pkNum = Product.objects.get(title=item.title).pk

            context['page_obj'] = get_paginate(request, items, 10)
            return render(request, 'userEnvironment/purchasedItems.html', context=context)

        elif PurchasedItemsModel.objects.latest('created_at').sort_by == '-':
            purchasedItemsList = PurchasedItemsModel.objects.filter(user=request.user).order_by('-created_at')
            items = purchasedItemsList
            for item in items:
                item.pkNum = Product.objects.get(title=item.title).pk
            context['page_obj'] = get_paginate(request, items, 10)
            return render(request, 'userEnvironment/purchasedItems.html', context=context)
        else:
            purchasedItemsList = PurchasedItemsModel.objects.filter(user=request.user).order_by('created_at')
            items = purchasedItemsList
            for item in items:
                item.pkNum = Product.objects.get(title=item.title).pk
            context['page_obj'] = get_paginate(request, items, 10)
            return render(request, 'userEnvironment/purchasedItems.html', context=context)
    except Exception as exc:
        return render(request, 'userEnvironment/purchasedItems.html')


def buy(request, overall_price):
    api = Api(merchant_id=1396424,
              secret_key='test')
    checkout = Checkout(api=api)
    data = {
        "currency": "USD",
        "amount": str(int(overall_price / 60))
    }
    url = checkout.url(data).get('checkout_url')
    context = {
        'url': url,
        'overall_price': overall_price
    }

    return render(request, 'userEnvironment/buy.html', context=context)


def basket(request):
    products = []

    amount_of_product = ProductInBasket.objects.filter(user=request.user).aggregate(Sum('number'))

    product_in_basket = ProductInBasket.objects.filter(user=request.user)
    for item in product_in_basket:
        products.append(Product.objects.get(title=item.product))

    for item in products:
        if ProductInBasket.objects.get(product=item.title):
            item.number = ProductInBasket.objects.get(product=item.title).number

    context = {
        'amount_of_product': amount_of_product,
        'products': products,
        'viewed_items_list': mostViewed(request)
    }

    return render(request, 'userEnvironment/basket.html', context=context)


def product_in_basket_to_model(request):
    return_dict = dict()
    py_obj = json.loads(request.body)

    try:
        if ProductInBasket.objects.filter(user=py_obj['user'], product=py_obj['product']):
            changing_field = ProductInBasket.objects.get(user=py_obj['user'], product=py_obj['product'])
            changing_field.number += int(py_obj['amount'])
            changing_field.save()
            changing_field.total_price = changing_field.price_per_item * changing_field.number
            changing_field.save()
        else:
            ProductInBasket.objects.create(user=py_obj['user'], product=py_obj['product'], number=int(py_obj['amount']),
                                           image=py_obj['image'], price_per_item=py_obj['price_per_item'],
                                           total_price=int(py_obj['price_per_item']) * int(py_obj['amount']))
    except Exception as exc:
        print(exc)
    finally:
        return_dict['amount_of_product'] = ProductInBasket.objects.filter(user=py_obj['user']).aggregate(Sum('number'))

        products_list = []
        for item in ProductInBasket.objects.filter(user=py_obj['user']):
            products_list.append(item.product)
        return_dict['products_in_basket'] = products_list

        return JsonResponse(return_dict)


def deletion_the_products_from_model_and_basket(request):
    return_dict = dict()
    py_obj = json.loads(request.body)

    try:
        ProductInBasket.objects.filter(user=py_obj['user'], product=py_obj['product']).delete()
    except Exception as exc:
        print(exc)
    finally:
        try:
            return_dict['amount_of_product'] = ProductInBasket.objects.filter(user=py_obj['user']).aggregate(
                Sum('number'))
            print(return_dict['amount_of_product'])
            return JsonResponse(return_dict)
        except Exception as exc:
            print(exc)


def toUserSelectionModel(request):
    return_dict = dict()
    py_obj = json.loads(request.body)

    try:
        if UserSelection.objects.filter(user=request.user, product=py_obj['product']):
            UserSelection.objects.filter(user=request.user, product=py_obj['product']).delete()
        else:
            UserSelection.objects.create(user=request.user, product=py_obj['product'], price_per_item=py_obj['price'],
                                         image=py_obj['image'])
    except Exception as exc:
        print(exc)
    finally:
        products_list = []
        for item in UserSelection.objects.filter(user=request.user):
            products_list.append(item.product)
        return_dict['products_in_user_selection'] = products_list
        return_dict['amount_of_product'] = UserSelection.objects.filter(user=request.user).aggregate(
            Sum('number'))
        return JsonResponse(return_dict)


def toUserSelection(request):
    products = []
    selected_product_list = UserSelection.objects.filter(user=request.user)
    for item in selected_product_list:
        products.append(Product.objects.get(user=request.user, title=item.product))

    amount_of_product = UserSelection.objects.filter(user=request.user).aggregate(Sum('number'))
    context = {
        'amount_of_product': amount_of_product,
        'products': products,
        'viewed_items_list': mostViewed(request)
    }
    return render(request, 'userEnvironment/userSelection.html', context=context)
