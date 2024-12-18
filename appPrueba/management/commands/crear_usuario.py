from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Crea un usuario de ejemplo'

    def handle(self, *args, **options):
        username = 'carlos'
        password = '123'
        email = 'carlos@gmail.com'

        # Crea el usuario
        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                'email': email,
                'first_name': 'carlos',
                'last_name': 'salazar',
            }
        )

        if created:
            user.set_password(password)  # Establece la contraseña
            user.save()  # Guarda el usuario en la base de datos
            self.stdout.write(self.style.SUCCESS(f'Usuario "{username}" creado exitosamente.'))
        else:
            self.stdout.write(self.style.WARNING(f'El usuario "{username}" ya existe.'))
