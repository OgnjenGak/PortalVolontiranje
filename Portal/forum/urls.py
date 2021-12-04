from django.urls import path
from . import views

urlpatterns = [
    path('diskusija/', views.diskusija, name='diskusija'),
    path('kreiranje/', views.kreiranjeDiskusije, name='kreiranjeDiskusije'),
    path('komentar/', views.dodajKomentar, name='dodajKomentar'),
]
