from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=250, db_index=True, verbose_name='Наименование категории')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    urlName = models.CharField(max_length=250, verbose_name='Имя ссылки')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['-title']


class Product(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    manufacturer = models.CharField(max_length=250, verbose_name='Производитель', blank=True)
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='%Y/%m/%d/', verbose_name='Фото', blank=True)
    price = models.IntegerField(blank=True, null=True, verbose_name='Цена')
    in_stock = models.BooleanField(default=True, verbose_name='В наличии')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликован')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE,
                                 verbose_name='Наименование категории')
    ram = models.CharField(max_length=250, verbose_name='Оперативная память', default='not')
    processor = models.CharField(max_length=250, verbose_name='Процессор', default='not')
    vram = models.CharField(max_length=250, verbose_name='Видеопамять', default='not')
    hdd_type = models.CharField(max_length=250, verbose_name='Тип жёского диска', default='not')
    tyre_section_width = models.CharField(max_length=250, verbose_name='Ширина профиля шины', default='not')
    tyre_section_height = models.CharField(max_length=250, verbose_name='Высота профиля шины', default='not')
    season = models.CharField(max_length=250, verbose_name='Сезон', default='not')
    diameter = models.CharField(max_length=250, verbose_name='Диаметр', default='not')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    sort_by = models.CharField(max_length=250, verbose_name='Упорядочить по', default='not')
    search_filter = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-title']


class ViewedItems(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='%Y/%m/%d/', verbose_name='Фото', blank=True)
    price = models.CharField(max_length=7, verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликован')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    number = models.IntegerField(default=1, verbose_name='Просмотрено раз')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Количесто просмотров товаров'
        verbose_name_plural = 'Количесто просмотров товара'
        ordering = ['-title']


class SearchQuery(models.Model):
    user = models.CharField(max_length=15, default='---',
                            verbose_name='Пользователь')
    category = models.CharField(max_length=250, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание', default='')
    sort_by = models.CharField(max_length=250, verbose_name='Упорядочить по', default='not')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликован')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Поисковый запрос'
        verbose_name_plural = 'Поисковые запросы'
