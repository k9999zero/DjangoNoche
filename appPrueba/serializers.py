from django.contrib.auth.models import User
from django.core.validators import EmailValidator
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Destination, Comment

from .models import Product,Category
from django.contrib.auth import authenticate

from .validators import validate_strong_password


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']  # Incluir solo los campos que necesitas de Category

class ProductSerializer(serializers.ModelSerializer):
    #category = CategorySerializer()  # Incluir la categoría como un objeto anidado (opcional)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'price', 'image']


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


class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'



class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_strong_password], style={"input_type": "password"}
    )
    password2 = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'email': {'required': True},
        }

    def validate(self, attrs):
        """
        Valida que las contraseñas coincidan.
        """
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Las contraseñas no coinciden."})
        return attrs

    def create(self, validated_data):
        """
        Crea un usuario con el modelo User y guarda la contraseña encriptada.
        """
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])  # Encripta la contraseña
        user.save()
        return user
