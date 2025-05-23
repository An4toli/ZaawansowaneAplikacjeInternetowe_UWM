from rest_framework import serializers
from .models import Produkt, Zamowienie

class ProduktSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produkt
        fields = '__all__'

class ZamowienieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zamowienie
        fields = '__all__'