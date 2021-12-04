from django.urls import path
from . import views

app_name = 'oglasi'
urlpatterns = [
    path('<int:id>/', views.detaljiOglasa, name='detaljiOglasa'),
    path('postavljanjeOglasa', views.postavljanjeOglasa, name='postavljanjeOglasa')
]
