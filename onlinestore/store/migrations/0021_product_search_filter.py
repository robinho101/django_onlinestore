# Generated by Django 4.1 on 2022-11-14 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_product_tyre_section_height'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='search_filter',
            field=models.BooleanField(default=False),
        ),
    ]
