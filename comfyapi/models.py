from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


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


class ShippingProfile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    county = models.CharField(max_length=150)
    town = models.CharField(max_length=150)
    contact = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        verbose_name_plural = 'ShippingProfiles'

    def __str__(self):
        return f'{self.owner.email}'


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.IntegerField()
    total_items = models.IntegerField()
    shipping_cost = models.IntegerField()
    order_totals = models.IntegerField()
    shippingprofile = models.ForeignKey(
        ShippingProfile, related_name='shipping_profile', on_delete=models.SET_NULL, null=True)
    paidAt = models.DateTimeField(auto_now=True)
    isPaid = models.BooleanField(default=False)
    deliveredAt = models.DateTimeField(auto_now=True)
    idDelivered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.owner.email}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name='order', on_delete=models.SET_NULL, null=True)
    identifier = models.CharField(max_length=100)
    name = models.CharField(max_length=150)
    amount = models.IntegerField()
    color = models.CharField(max_length=10)
    image = models.URLField()

    def __str__(self):
        return f"{self.name}"
