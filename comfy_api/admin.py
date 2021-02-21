from django.contrib import admin
from .models import Product, Color, Image

admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Color)
