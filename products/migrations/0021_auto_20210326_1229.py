# Generated by Django 3.1.7 on 2021-03-26 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_auto_20210326_1228'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='price_item',
            options={'ordering': ['price', 'item_owner']},
        ),
    ]
