from django.shortcuts import render
from rest_framework import viewsets
from .models import Produkt, Zamowienie
from .serializers import ProduktSerializer, ZamowienieSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

class ProduktViewSet(viewsets.ModelViewSet):
    queryset = Produkt.objects.all()
    serializer_class = ProduktSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ZamowienieViewSet(viewsets.ModelViewSet):
    queryset = Zamowienie.objects.all()
    serializer_class = ZamowienieSerializer
    permission_classes = [IsAuthenticated]
