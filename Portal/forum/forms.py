from django import forms

from .models import Diskusija, Kategorija_diskusije, Komentar


class DiskusijaCreateForm(forms.ModelForm):
    class Meta:
        model = Diskusija
        fields = ["naziv", "tekst", "vidljivost", "vidljivost_za_org", 'kategorija']

        # exclude = ["autor", "datum"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        self.fields['naziv'].widget.attrs.update(
            {
                'placeholder': 'Упишите назив'
            }
        )
        self.fields['naziv'].label = "Назив дискусије"
        self.fields['tekst'].label = "Текст дискусије"
        self.fields['vidljivost'].label = "Видљивост за кориснике"
        self.fields['vidljivost_za_org'].label = "Видљивост за организације"
        self.fields['kategorija'].label = "Одеберите категорију дискусије"



class KategorijaDiskusijeCreateForm(forms.ModelForm):
    class Meta:
        model = Kategorija_diskusije
        fields = ["naziv"]
        labels = {
            "naziv": "Назив"
        }
        widgets = {
            "naziv": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            )
        }


class KomentarCreateForm(forms.ModelForm):
    class Meta:
        model = Komentar
        fields = ['sadrzaj']
        labels = {
            "sadrzaj": ""
        }
        widgets = {
            "sadrzaj": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Упишите свој коментар"
                }
            )
        }



