# Generated by Django 3.1.7 on 2021-02-22 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comfyapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='company',
            field=models.CharField(max_length=150),
        ),
        migrations.DeleteModel(
            name='Company',
        ),
    ]
