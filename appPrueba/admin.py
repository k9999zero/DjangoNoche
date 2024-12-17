from django.contrib import admin
from .models import Destination, Comment

# Configurar modelos en el admin
@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')  # Mostrar nombre y fecha
    search_fields = ('name',)  # Búsqueda por nombre

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'destination', 'rating', 'created_at')  # Información importante
    list_filter = ('rating', 'created_at')  # Filtros por puntuación y fecha
    search_fields = ('user__username', 'destination__name')  # Búsqueda por usuario y destino
