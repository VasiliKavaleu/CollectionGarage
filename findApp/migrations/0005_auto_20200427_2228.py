# Generated by Django 3.0.5 on 2020-04-27 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findApp', '0004_auto_20200427_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='price',
            field=models.CharField(max_length=15, verbose_name='Цена'),
        ),
    ]
