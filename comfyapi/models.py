from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    company = models.CharField(max_length=150)
    category = models.CharField(max_length=150, default='home')
    shipping = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    description = models.TextField(max_length=250)
    countInStock = models.IntegerField(default=0)
    stars = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    reviews = models.IntegerField(default=0)

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
