from django.shortcuts import render
from django.http import HttpResponse
from Czujniki.models import Czujnik

def wszystkie(request):
    return HttpResponse(["<h1>",[[f.id, f.nazwa, f.cena] for f in Czujnik.objects.all()],"</h1>"])

def szczegoly(request,czujnik_id):
    f = Czujnik.objects.get(id=czujnik_id)
    return HttpResponse(
        "<h3> Nazwa Czujnika: {},</br> cena: {}, </br> opis: {} </h3>"
        .format(f.nazwa, f.cena, f.opis))
