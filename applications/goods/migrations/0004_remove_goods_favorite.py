# Generated by Django 4.0.3 on 2022-03-25 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_goods_favorite_goods_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='favorite',
        ),
    ]
