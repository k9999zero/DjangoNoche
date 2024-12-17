from django.core.exceptions import ValidationError
import re

def validate_strong_password(password):
    """
    Valida que la contraseña cumpla con los siguientes requisitos:
    - Al menos 8 caracteres
    - Contiene al menos un número
    - Contiene al menos una letra mayúscula
    - Contiene al menos una letra minúscula
    - Contiene al menos un carácter especial
    """
    if len(password) < 8:
        raise ValidationError("La contraseña debe tener al menos 8 caracteres.")

    if not re.search(r'\d', password):
        raise ValidationError("La contraseña debe contener al menos un número.")

    if not re.search(r'[A-Z]', password):
        raise ValidationError("La contraseña debe contener al menos una letra mayúscula.")

    if not re.search(r'[a-z]', password):
        raise ValidationError("La contraseña debe contener al menos una letra minúscula.")

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        raise ValidationError("La contraseña debe contener al menos un carácter especial.")
