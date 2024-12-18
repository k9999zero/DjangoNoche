from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

class Category(models.Model):
    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.named

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.name

#para lso destinos
class Destination(models.Model):
    name = models.CharField(max_length=200, blank=False)  # Nombre del destino
    description = models.TextField(blank=True)  # Descripción del destino
    location = models.TextField(blank=True)
    image = models.ImageField(upload_to='destination_images/')  # Imagen del destino
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación

    def __str__(self):
        return self.name



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el usuario
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='comments')  # Relación con el destino
    comment = models.TextField(blank=False)  # Comentario del usuario
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1, "La puntuación mínima es 1."),
            MaxValueValidator(5, "La puntuación máxima es 5.")
        ]
    )  # Puntuación (1 a 5)
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha del comentario

    def __str__(self):
        return f"Comentario de {self.user.username} - {self.destination.name}"
