from django.db import models
from django.contrib.auth.models import User


class Anketa(models.Model):
    naziv_ankete = models.CharField(max_length=50)
    vidljivost_ankete = models.BooleanField(default=False)
    pitanje = models.CharField(max_length=200, null=True)
    autor_ankete = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.naziv_ankete


skala = (
        (1, "У потпуности се не слажем."),
        (2, "Делимично се не слажем."),
        (3, "Нити се слажем, нити се не слажем."),
        (4, "Делимично се слажем."),
        (5, "У потпуности се слажем."),
        (0, "Не желим да одговорим.")
        )


class Stavka(models.Model):
    pitanje = models.ForeignKey(Anketa, on_delete=models.CASCADE, null=True)
    glasovi = models.PositiveSmallIntegerField(default=3, choices=skala)
    ispitanik = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
