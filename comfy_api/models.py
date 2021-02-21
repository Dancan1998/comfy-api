from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=250)


class Image(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media')
    default = models.BooleanField(default=False)


class Color(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
