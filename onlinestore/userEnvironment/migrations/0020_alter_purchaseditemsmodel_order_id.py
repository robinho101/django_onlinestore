# Generated by Django 4.1 on 2022-11-05 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userEnvironment', '0019_alter_purchaseditemsmodel_sort_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseditemsmodel',
            name='order_id',
            field=models.CharField(default='---', max_length=30, verbose_name='Идентификатор заказа'),
        ),
    ]
