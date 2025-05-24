from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Produkt, Kategoria, Producent


class ProduktApiTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.kategoria = Kategoria.objects.create(nazwa='Testowa Kategoria')
        self.producent = Producent.objects.create(nazwa='Testowy Producent', kraj='Polska')

        # logowanie JWT i pobranie access token
        response = self.client.post('/api/token/', {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.access_token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_dodanie_produktu_po_zalogowaniu(self):
        url = '/czujniki/produkty/'
        data = {
            "nazwa": "Test Produkt",
            "opis": "Opis testowy",
            "cena": "123.45",
            "dostepnosc": True,
            "kategoria": self.kategoria.id,
            "producent": self.producent.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Produkt.objects.count(), 1)

    def test_get_lista_produktow_bez_logowania(self):
        # najpierw usuń nagłówek autoryzacji, żeby symulować anonimowego użytkownika
        self.client.credentials()

        Produkt.objects.create(
            nazwa="Test Produkt",
            opis="Opis testowy",
            cena=123.45,
            dostepnosc=True,
            kategoria=self.kategoria,
            producent=self.producent
        )
        response = self.client.get('/czujniki/produkty/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
