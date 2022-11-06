from django.db import models
from django.contrib.auth.models import User
from store.models import *


# Create your models here.

class ProductInBasket(models.Model):
    user = models.CharField(max_length=15, default='---',
                            verbose_name='Пользователь')
    image = models.ImageField(max_length=1000, upload_to='', verbose_name='Фото', blank=True)
    product = models.CharField(max_length=500, default='---',
                               verbose_name='Товар')
    number = models.IntegerField(default=0, verbose_name='Количество')
    price_per_item = models.IntegerField(default=0, verbose_name='Цена за товар')
    total_price = models.IntegerField(default=0, verbose_name='Итоговая цена')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False,
                                      verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True,
                                      verbose_name='Обновлено')

    def __str__(self):
        return self.product

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'


class UserSelection(models.Model):
    user = models.CharField(max_length=15, default='---',
                            verbose_name='Пользователь')
    image = models.ImageField(max_length=1000, upload_to='', verbose_name='Фото', blank=True)
    product = models.CharField(max_length=500, default='---',
                               verbose_name='Товар')
    price_per_item = models.IntegerField(default=0, verbose_name='Цена за товар')
    number = models.IntegerField(default=1, verbose_name='Количество')
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Обновлено')

    def __str__(self):
        return self.product

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'


class PurchasedItemsModel(models.Model):
    order_id = models.CharField(max_length=30, default='---',
                                verbose_name='Идентификатор заказа')
    user = models.CharField(max_length=15, default='---',
                            verbose_name='Пользователь')
    image = models.ImageField(max_length=1000, upload_to='', verbose_name='Фото', blank=True)
    title = models.CharField(max_length=500, default='---',
                             verbose_name='Товар')
    price = models.IntegerField(default=0, verbose_name='Цена за товар')
    amount = models.IntegerField(default=1, verbose_name='Количество')
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Обновлено')
    sort_by = models.CharField(max_length=250, verbose_name='Сортировать по', default='not')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Оплаченный товар'
        verbose_name_plural = 'Оплаченные товары'
