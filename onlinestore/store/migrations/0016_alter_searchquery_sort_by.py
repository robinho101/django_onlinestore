# Generated by Django 4.1 on 2022-11-03 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchquery',
            name='sort_by',
            field=models.CharField(default='not', max_length=250, verbose_name='Сортировать по'),
        ),
    ]