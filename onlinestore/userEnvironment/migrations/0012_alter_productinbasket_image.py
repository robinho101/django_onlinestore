# Generated by Django 4.1 on 2022-10-21 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userEnvironment', '0011_alter_productinbasket_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinbasket',
            name='image',
            field=models.ImageField(blank=True, max_length=1000, upload_to='./', verbose_name='Фото'),
        ),
    ]