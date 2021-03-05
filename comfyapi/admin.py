from django.contrib import admin
from .models import Product, Image, Color, ShippingProfile, Order, OrderItem

admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Color)
admin.site.register(ShippingProfile)
admin.site.register(OrderItem)
admin.site.register(Order)
