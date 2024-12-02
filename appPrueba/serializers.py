from django.contrib.auth.models import User
from django.core.validators import EmailValidator
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Product
from django.contrib.auth import authenticate
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  # Incluye todos los campos del modelo

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, error_messages= {
    'required': 'El correo electronico es un campo requerido',
    'invalid': 'Correo electronico inválido',
    'blank': 'El correo electronico es un campo requerido',
})
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        # Obtener el email y la contraseña del usuario
        email = data.get('email')
        password = data.get('password')

        # Validar que ambos campos están presentes
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

        # Verificar si el usuario está activo
        if not user.is_active:
            raise serializers.ValidationError({"auth_error":"User account is disabled."})

        # Añadir el usuario al contexto para usarlo más adelante
        data['user'] = user
        return data