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


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=150, min_length=3)
    password = serializers.CharField(
        max_length=255, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name','tokens']
        read_only_fields = ['first_name', 'last_name', 'tokens']

    def validate(self, attrs):
        """Login a user with email and password and return the refresh and access token for the user"""
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        user = auth.authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account inactive, contact admin')
        if not user.email:
            raise AuthenticationFailed({'email':'Wrong email address'})
        if not user.password:
            raise AuthenticationFailed({'password':'Wrong password'})

        return {
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'tokens': user.tokens()
        }