from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Crea un usuario de ejemplo'

    def handle(self, *args, **options):
        username = 'GojanDed'
        password = '75987474_GojanDed'
        email = 'gojanded@correo.com'

        # Crea el usuario
        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                'email': email,
                'first_name': 'Erick',
                'last_name': 'Candia',
            }
        )

        if created:
            user.set_password(password)  # Establece la contraseña
            user.save()  # Guarda el usuario en la base de datos
            self.stdout.write(self.style.SUCCESS(f'Usuario "{username}" creado exitosamente.'))
        else:
            self.stdout.write(self.style.WARNING(f'El usuario "{username}" ya existe.'))
