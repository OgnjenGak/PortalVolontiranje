from django import forms
from .models import Oglas


class Forma_postavljanja_oglasa(forms.ModelForm):
    class Meta:
        model = Oglas

        fields = [
            "naslov", "tekst", "vidljivost",
        ]

    def __init__(self, *args, **kwargs):
        super(Forma_postavljanja_oglasa, self).__init__(*args, **kwargs)
        for fieldname in ['naslov']:
            self.fields[fieldname].label = 'Наслов'
        for fieldname in ['tekst']:
            self.fields[fieldname].label = 'Текст'
        for fieldname in ['vidljivost']:
            self.fields[fieldname].label = 'Видљивост'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
