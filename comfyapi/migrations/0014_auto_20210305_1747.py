# Generated by Django 3.1.7 on 2021-03-06 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comfyapi', '0013_order_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='orderItem',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order', to='comfyapi.order'),
        ),
    ]
