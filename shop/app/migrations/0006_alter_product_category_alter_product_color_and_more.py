# Generated by Django 4.2.13 on 2024-07-06 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(max_length=60),
        ),
    ]
