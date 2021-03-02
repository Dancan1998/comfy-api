from rest_framework import serializers
from .models import Product, Image, ShippingProfile


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


class ShippingProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShippingProfile
        fields = '__all__'
        read_only_fields = ['owner']

    def validate(self, attrs):
        county = attrs.get('county', '')
        town = attrs.get('town', '')
        contact = attrs.get('contact', '')
        if county == "":
            raise serializers.ValidationError(
                {'county': 'County cannot be null'})
        if town == "":
            raise serializers.ValidationError({'town': "Town can not be null"})
        return attrs

    def create(self, validated_data):
        return ShippingProfile.objects.create(**validated_data)
