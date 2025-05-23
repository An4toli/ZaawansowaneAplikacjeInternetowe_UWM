from django.contrib import admin
from .models import Produkt, Kategoria, Producent, Zamowienie

@admin.register(Produkt)
class ProduktAdmin(admin.ModelAdmin):
    list_display = ('id', 'nazwa', 'cena', 'dostepnosc', 'kategoria', 'producent')
    search_fields = ('nazwa',)
    list_filter = ('kategoria', 'producent')

@admin.register(Zamowienie)
class ZamowienieAdmin(admin.ModelAdmin):
    list_display = ('id', 'uzytkownik', 'status', 'data')
    list_filter = ('status', 'data')
    filter_horizontal = ('produkty',)  # dla lepszej obsługi ManyToMany w panelu


admin.site.register(Kategoria)
admin.site.register(Producent)
