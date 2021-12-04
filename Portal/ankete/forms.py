from .models import Stavka, Anketa
from django import forms


class AnketeCreateForm(forms.ModelForm):
    class Meta:
        model = Anketa
        fields = ["vidljivost_ankete", "naziv_ankete", 'pitanje']

    def __init__(self, *args, **kwargs):
        super(AnketeCreateForm, self).__init__(*args, **kwargs)
        self.fields['naziv_ankete'].label = ''
        self.fields['naziv_ankete'].widget.attrs.update(
            {
                'placeholder': 'Упишите назив анкете...',
                'class': 'form-control',
            }
        )
        for fieldname in ['vidljivost_ankete']:
            self.fields[fieldname].label = 'Означите поље уколико желите да анкета буде јавна. '
        self.fields['vidljivost_ankete'].widget.attrs.update(
            {
                'class': 'form-check-input',
            }
        )
        self.fields['pitanje'].label = ''
        self.fields['pitanje'].widget.attrs.update(
            {
                'placeholder': 'Упишите своје питење...',
                'class': 'form-control',
            }
        )


class Glasovi(forms.ModelForm):
    class Meta:
        model = Stavka
        fields = ['glasovi']
        labels = {'glasovi': 'Ваш одговор је: '}

    def __init__(self, *args, **kwargs):
        super(Glasovi, self).__init__(*args, **kwargs)

        self.fields['glasovi'].widget.attrs.update(
            {
                'class': 'form-control',
            }
        )
