from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    company = models.CharField(max_length=150)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=150)
    product = models.ForeignKey(
        Product, related_name='images', on_delete=models.CASCADE)
    image = models.URLField()

    def __str__(self):
        return f"{self.name}"


class Color(models.Model):
    name = models.CharField(max_length=150)
    product = models.ForeignKey(
        Product, related_name='colors', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
