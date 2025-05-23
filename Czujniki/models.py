from django.db import models
from django.contrib.auth.models import User

class Kategoria(models.Model):
    nazwa = models.CharField(max_length=100)

#Klasa meta zeby nazwy na panelu admina wygladaly normalnie
    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"

    def __str__(self):
        return self.nazwa

class Producent(models.Model):
    nazwa = models.CharField(max_length=100)
    kraj = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Producent"
        verbose_name_plural = "Producenci"

    def __str__(self):
        return self.nazwa
# Create your models here.
class Produkt(models.Model):
    nazwa = models.CharField(max_length=100)
    opis = models.TextField()
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    dostepnosc = models.BooleanField(default=True)
    zdjecie = models.ImageField(upload_to='produkty/', blank=True, null=True)
    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE)
    producent = models.ForeignKey(Producent, on_delete=models.CASCADE)


    class Meta:
        verbose_name = "Produkt"
        verbose_name_plural = "Produkty"

    def __str__(self):
        return "{} ({})".format(self.nazwa, str(self.cena))

class Zamowienie(models.Model):
        STATUSY = [
            ('nowe', 'Nowe'),
            ('zrealizowane', 'Zrealizowane'),
            ('anulowane','Anulowane'),
        ]
        uzytkownik=models.ForeignKey(User, on_delete=models.CASCADE)
        produkty= models.ManyToManyField(Produkt)
        status = models.CharField(max_length=20, choices=STATUSY, default='nowe')
        data = models.DateTimeField(auto_now_add=True)

        class Meta:
            verbose_name = "Zamówienie"
            verbose_name_plural = "Zamówienia"

        def __str__(self):
            return f"Zamowienie {self.id} - {self.uzytkownik.username}"
