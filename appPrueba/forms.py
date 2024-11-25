from django import forms

class EmailLoginForm(forms.Form):
    email = forms.EmailField(label="Correo Electrónico", widget=forms.EmailInput(attrs={
        'placeholder': 'Ingresa tu correo',
        'class': 'form-control',
    }),
    required=True,
    error_messages={
            'required': 'probando.',
            'invalid': 'Hola2.',
        }
    )
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={
        'placeholder': 'Ingresa tu contraseña',
        'class': 'form-control'
    }),
    required=True
    )