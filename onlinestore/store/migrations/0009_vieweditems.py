# Generated by Django 4.1 on 2022-10-27 21:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0008_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewedItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(blank=True, upload_to='%Y/%m/%d/', verbose_name='Фото')),
                ('price', models.CharField(max_length=7, verbose_name='Цена')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Опубликован')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('number', models.IntegerField(default=1, verbose_name='Просмотрено раз')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['-title'],
            },
        ),
    ]