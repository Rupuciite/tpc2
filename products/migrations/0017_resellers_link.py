# Generated by Django 3.1.7 on 2021-03-25 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20210324_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='resellers',
            name='link',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]