from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    password1 = serializers.CharField(
        max_length=68, min_length=6, write_only=True)


    class Meta:
        model = User
        fields = ['email', 'password', 'password1', 'first_name','last_name']

    def validate(self, attrs):
        """Validate the email"""
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        password1 = attrs.get('password1', '')
        if not email:
            raise serializers.ValidationError({'email':'The email address is not valid'})
        if len(password) < 6:
            raise serializers.ValidationError({'password':'Password has to be more than 6 characters'})
        if(password != password1):
            raise serializers.ValidationError({'password':'Passwords should match'})

        return attrs

    def create(self, validated_data):
        """Create a user with validated data"""
        return User.objects.create_user(**validated_data)
