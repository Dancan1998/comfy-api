from django.shortcuts import render
from .serializers import ProductSerializer, ShippingProfileSerializer, OrderSerializer
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Product, ShippingProfile, Order
from .permissions import IsOwner


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ShippingProfileView(generics.ListCreateAPIView):
    serializer_class = ShippingProfileSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        if not ShippingProfile.objects.filter(owner=self.request.user).exists():
            serializer.save(owner=self.request.user)
        else:
            return Response({'message': 'User already has shipping profile'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        return ShippingProfile.objects.filter(owner=self.request.user)


class ShippingProfileDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = ShippingProfileSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return ShippingProfile.objects.filter(owner=self.request.user.id)


class OrderView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=self.request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        return Order.objects.filter(owner=self.request.user)
