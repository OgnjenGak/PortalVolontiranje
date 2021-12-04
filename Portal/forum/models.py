from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Kategorija_diskusije(models.Model):
    naziv = models.CharField(max_length=100)

    def __str__(self):
        return self.naziv


class Diskusija(models.Model):
    naziv = models.CharField(max_length=100, unique=True)
    tekst = models.TextField()
    datum = models.DateTimeField(auto_now_add=True)
    V = (
        (1, 'Сви'),
        (2, 'Само логовани корисници'),
    )
    vidljivost = models.PositiveSmallIntegerField(default=1, choices=V)
    VZO = (
        (1, 'Сви'),
        (2, 'Волонтери'),
    )
    vidljivost_za_org = models.PositiveSmallIntegerField(default=1, choices=VZO)
    kategorija = models.ForeignKey(Kategorija_diskusije, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


class Komentar(models.Model):
    sadrzaj = models.TextField()
    datum = models.DateTimeField(auto_now_add=True)
    diskusija = models.ForeignKey(Diskusija, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.diskusija.naziv + ' - ' + str(self.datum.strftime("%d %b %Y"))
