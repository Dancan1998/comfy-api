# Generated by Django 3.1.7 on 2021-03-02 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comfyapi', '0008_shippingprofile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shippingprofile',
            options={'verbose_name_plural': 'ShippingProfiles'},
        ),
        migrations.AlterField(
            model_name='shippingprofile',
            name='phone_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
