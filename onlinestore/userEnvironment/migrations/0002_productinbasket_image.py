# Generated by Django 4.1 on 2022-10-07 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userEnvironment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinbasket',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/%Y/%m/%d/', verbose_name='Фото'),
        ),
    ]
