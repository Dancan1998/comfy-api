from rest_framework import serializers
from .models import Product, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'name', 'image']


class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    colors = serializers.StringRelatedField(many=True)

    class Meta:
        model = Product
        fields = '__all__'
