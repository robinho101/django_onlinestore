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
    price = models.CharField(max_length=7, verbose_name='Цена')
    in_stock = models.BooleanField(default=True, verbose_name='В наличии')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликован')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE,
                                 verbose_name='Наименование категории')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-title']
