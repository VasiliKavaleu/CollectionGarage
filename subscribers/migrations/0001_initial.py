# Generated by Django 3.0.5 on 2020-05-06 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('findApp', '0007_auto_20200506_1109'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100, unique=True, verbose_name='E-mail')),
                ('password', models.CharField(max_length=100, verbose_name='Пароль')),
                ('is_activ', models.BooleanField(default=True, verbose_name='Получать рассылку?')),
                ('carModel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='findApp.CarModel', verbose_name='Модель авто')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='findApp.City', verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Подписчик',
                'verbose_name_plural': 'Подписчики',
            },
        ),
    ]