from django.db import models
from django.contrib.auth.models import User


class Oglas(models.Model):
    naslov = models.CharField(max_length=50)
    tekst = models.TextField(blank=True)
    datum = models.DateTimeField(auto_now_add=True)
    opcije = (
        (1, 'Сви'),
        (2, 'Волонтери'),
    )
    vidljivost = models.PositiveSmallIntegerField(default=1, choices=opcije)
    za_brisanje = models.BooleanField(default=False)
    arhiviran = models.BooleanField(default=False)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
