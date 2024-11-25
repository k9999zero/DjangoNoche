# views.py
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import EmailLoginForm
from django.contrib.auth.models import User

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
