# Generated by Django 5.0.2 on 2024-02-23 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=30, verbose_name='название')),
            ],
            options={
                'verbose_name': 'город',
                'verbose_name_plural': 'города',
            },
        ),
    ]
