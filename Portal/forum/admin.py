from django.contrib import admin
from .models import Diskusija, Kategorija_diskusije, Komentar

# Register your models here.

admin.site.register(Diskusija)
admin.site.register(Kategorija_diskusije)
admin.site.register(Komentar)
