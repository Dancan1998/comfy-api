# Generated by Django 3.1.7 on 2021-02-22 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comfyapi', '0004_product_shipping'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]