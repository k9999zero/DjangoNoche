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
from .serializers import LoginSerializer
#rest
from rest_framework import permissions, viewsets, status

from tutorial.quickstart.serializers import GroupSerializer, UserSerializer

from .utils import custom_response

'''
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
'''
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
            return Response({
                'refresh': str(refresh),
                'access': access,
                'user': {
                    'id': user.id,
                    'email': user.email,
                    'username': user.username,
                }
            }, status=status.HTTP_200_OK)

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
