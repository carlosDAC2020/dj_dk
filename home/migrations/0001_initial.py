# Generated by Django 4.1.4 on 2022-12-30 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=20)),
                ('units_available', models.IntegerField(default=0)),
                ('worth_unit', models.IntegerField(default=0)),
                ('product_photo', models.ImageField(upload_to='products/images')),
            ],
        ),
    ]
