from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

class Category(models.Model):
    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True)
    price = models.IntegerField()
    calidad = models.CharField(max_length=200, blank=True)
    stock = models.CharField(max_length=200, blank=True)
    descripcion = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='product_images/')  # Corregida la indentación

    def __str__(self):
        return self.name
