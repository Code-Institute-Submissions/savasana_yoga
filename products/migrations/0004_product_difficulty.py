# Generated by Django 3.2.5 on 2021-07-17 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210716_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='difficulty',
            field=models.CharField(choices=[('BEGINNER', 'Beginner'), ('INTERMEDIATE', 'Intermediate'), ('ADVANCED', 'Advanced')], default='Beginner', max_length=32),
        ),
    ]