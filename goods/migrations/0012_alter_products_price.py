# Generated by Django 4.2.7 on 2024-03-28 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0011_alter_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Цена'),
        ),
    ]