from django.shortcuts import render
from .serializers import ProductSerializer, ShippingProfileSerializer
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Product, ShippingProfile
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
        serializer.errors
        serializer.save(user=self.request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def get_queryset(self):
    #     return ShippingProfile.objects.filter(user=self.request.user)
