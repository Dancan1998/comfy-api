# Generated by Django 3.1.7 on 2021-03-02 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comfyapi', '0011_remove_shippingprofile_phone_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingprofile',
            name='contact',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
