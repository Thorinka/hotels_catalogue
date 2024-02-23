# Generated by Django 5.0.2 on 2024-02-23 16:20

import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=60, verbose_name='название отеля')),
                ('address', models.CharField(max_length=150, verbose_name='адрес')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='электронная почта')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities.city', verbose_name='город')),
            ],
            options={
                'verbose_name': 'отель',
                'verbose_name_plural': 'отели',
            },
        ),
    ]
