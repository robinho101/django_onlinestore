import json

from django.core.paginator import *
from django.db.models import *
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.views.generic import ListView, DetailView, CreateView
from store.models import *
from .models import *


# Create your views here.

def basket(request):
    amount_of_product = ProductInBasket.objects.filter(user=request.user).aggregate(Sum('number'))

    product_in_basket = ProductInBasket.objects.filter(user=request.user)

    paginator = Paginator(product_in_basket, 5)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)

    context = {
        'amount_of_product': amount_of_product,
        'product_in_basket': product_in_basket,
        'page_obj': page_obj
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
    selected_product_list = UserSelection.objects.filter(user=request.user)
    amount_of_product = UserSelection.objects.filter(user=request.user).aggregate(Sum('number'))
    context = {
        'selected_product_list': selected_product_list,
        'amount_of_product': amount_of_product
    }
    return render(request, 'userEnvironment/userSelection.html', context=context)
