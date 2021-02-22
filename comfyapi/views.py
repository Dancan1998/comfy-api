from django.shortcuts import render
from .serializers import ProductSerializer
from rest_framework import generics
from .models import Product


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
