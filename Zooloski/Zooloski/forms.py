from django import forms
from .models import Nastamba

class NastambaForm(forms.ModelForm):
    class Meta:
        model = Nastamba
        fields = ['vrsta', 'ime', 'centralna_tocka_lat', 'centralna_tocka_lng', 'opis', 'biljke', 'stabla', 'sekundarne_zivotinje', 'evidencija_prisutnosti']
