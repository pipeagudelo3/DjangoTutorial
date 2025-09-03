from rest_framework import serializers
from pages.models import Product  # Ajusta si el modelo está en otra app

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description']  # Agrega los campos relevantes
