# Generated by Django 3.2.5 on 2021-07-17 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_difficulty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='difficulty',
        ),
    ]
