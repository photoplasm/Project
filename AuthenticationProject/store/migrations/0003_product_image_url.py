# Generated by Django 5.1.1 on 2024-10-07 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_product_image_remove_product_stock_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.TextField(blank=True),
        ),
    ]
