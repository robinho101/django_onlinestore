# Generated by Django 4.1 on 2022-11-03 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userEnvironment', '0017_alter_userselection_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseditemsmodel',
            name='sort_by',
            field=models.CharField(blank=True, max_length=250, verbose_name='Сортировать по'),
        ),
    ]