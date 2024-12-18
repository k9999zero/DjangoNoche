from django.contrib.auth.models import User
from django.core.validators import EmailValidator
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Product, Category
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']  # Incluir solo los campos que necesitas de Category

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    category_name = serializers.SerializerMethodField()  # Campo adicional para el nombre de la categoría

    class Meta:
        model = Product
        fields = ['id', 'category', 'category_name', 'name', 'price', 'image', 'description']

    def get_category_name(self, obj):
        return obj.category.name if obj.category else None  # Retorna el nombre de la categoría

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, error_messages={
        'required': 'El correo electronico es un campo requerido',
        'invalid': 'Correo electronico inválido',
        'blank': 'El correo electronico es un campo requerido',
    })
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            raise serializers.ValidationError("Email and password are required.")

        try:
            user = User.objects.get(email=email)
            username = user.username
        except User.DoesNotExist:
            username = None

        user = authenticate(username=username, password=password)

        if not user:
            raise serializers.ValidationError({"auth_error": "Invalid credentials."})

        if not user.is_active:
            raise serializers.ValidationError({"auth_error": "User  account is disabled."})

        data['user'] = user
        return data

User  = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']  # Add any other fields you need
