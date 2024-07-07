# Generated by Django 4.2.13 on 2024-07-06 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('title', 'color')},
        ),
    ]
