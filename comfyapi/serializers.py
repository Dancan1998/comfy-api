from rest_framework import serializers
from .models import Product, Image, ShippingProfile, Order, OrderItem


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
    owner = serializers.SerializerMethodField()

    class Meta:
        model = ShippingProfile
        fields = '__all__'
        read_only_fields = ['owner']

    def get_owner(self, obj):
        request = self.context.get('request', None)
        if request:
            return f"{request.user.first_name} {request.user.last_name}"

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


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
        read_only_fields = ['order']


class OrderSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()
    order = OrderItemSerializer(many=True)
    # shippingprofile = ShippingProfileSerializer()

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['owner', 'order',  'shippingprofile']

    def get_owner(self, obj):
        request = self.context.get('request', None)
        if request:
            return f"{request.user.first_name} {request.user.last_name}"

    def create(self, validated_data):
        orders_data = validated_data.pop('order')
        order = Order.objects.create(**validated_data)
        for order_data in orders_data:
            OrderItem.objects.create(order=order, **order_data)
        return order
