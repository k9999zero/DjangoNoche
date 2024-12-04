# views.py
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .forms import EmailLoginForm
from django.contrib.auth.models import User
from rest_framework.views import APIView

from .models import Product, Category
from .serializers import LoginSerializer, ProductSerializer, CategorySerializer
#rest
from rest_framework import permissions, viewsets, status

from tutorial.quickstart.serializers import GroupSerializer, UserSerializer

from .utils import custom_response

class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Category.objects.all()  # Obtener todos los productos
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Product.objects.select_related('category')
    serializer_class = ProductSerializer

    # Sobrescribir el método create para personalizar la creación
    def create(self, request, *args, **kwargs):
        # Llamar al método padre para la creación normal
        response = super().create(request, *args, **kwargs)

        # Personalizar la respuesta si es necesario
        response.data['message'] = 'Producto creado exitosamente'

        return response

    # Sobrescribir el método update para personalizar la actualización
    def update(self, request, *args, **kwargs):
        # Aquí puedes añadir lógica personalizada antes de la actualización
        response = super().update(request, *args, **kwargs)
        response.data['message'] = 'Producto actualizado exitosamente'
        return response

    # Sobrescribir el método destroy para personalizar la eliminación
    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return custom_response(True, {
            'message': "Datos eliminados"
        }, 200)

    # Sobrescribir el método list para personalizar la lista
    def list(self, request, *args, **kwargs):

        response = super().list(request, *args, **kwargs)
        # Aseguramos que estamos trabajando con un diccionario
        '''
        response.data = {
            "message": "Lista de productos obtenida con éxito",
            "products": response.data  # Añadimos la lista de productos aquí
        }
        return response
        '''
        return custom_response(True, response.data, 200)

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']

            # Generar los tokens usando Simple JWT
            refresh = RefreshToken.for_user(user)
            access = str(refresh.access_token)

            # Respuesta personalizada
            return custom_response(True,{
                'refresh': str(refresh),
                'access': access,
                'user': {
                    'id': user.id,
                    'email': user.email,
                    'username': user.username,
                }
            }, 200)

        return custom_response(
            success=False,
            body=serializer.errors,  # Enviar los errores de validación
            code=400
        )
#rest

class CustomLoginView(View):
    template_name = 'login.html'

    def get(self, request):
        form = EmailLoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = EmailLoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            # Buscar usuario por email
            try:
                user = User.objects.get(email=email)
                username = user.username
            except User.DoesNotExist:
                username = None

            # Autenticar usuario
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Email o contraseña incorrectos.")
        else:
            messages.error(request, "Formulario inválido.")

        return render(request, self.template_name, {'form': form})
