from django.contrib import admin
from .models import Organizacija, Volonter, Drzava, Mesto, Ulica, Interesovanje, DodatniPodaci

from import_export.admin import ImportExportModelAdmin

# Register your models here.


class IEAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass


admin.site.register(Organizacija)
admin.site.register(Volonter)
admin.site.register(Drzava, IEAdmin)
admin.site.register(Mesto, IEAdmin)
admin.site.register(Ulica, IEAdmin)
admin.site.register(Interesovanje)
admin.site.register(DodatniPodaci)
