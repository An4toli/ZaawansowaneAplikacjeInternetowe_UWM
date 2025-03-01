from django.db import models

# Create your models here.
class Czujnik(models.Model):
    nazwa = models.CharField(max_length=100, blank=False, default="")
    napiecieZasilania = models.PositiveSmallIntegerField(blank=False)
    rodzajZasilania = models.CharField(max_length=100, blank=False)
    opis = models.TextField(default="")
    cena = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return "{} ({})".format(self.nazwa, str(self.cena))