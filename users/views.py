from rest_framework import generics, status, views
from rest_framework.response import Response
from .serializers import RegisterSerializer,LoginSerializer
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.conf import settings
from rest_framework import permissions
User = get_user_model()


class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        """"Get data via post and then push it to the serializer to handle for validation and save """
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.errors
        serializer.save()
        user_data = serializer.data

        return Response(user_data, status=status.HTTP_201_CREATED)

class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        """Login a user with valid data. Send the data to the serializer for validation"""
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)