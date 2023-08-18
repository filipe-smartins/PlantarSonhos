from django import forms
from .models import CorrecaoMonetaria


class CorrecaoMonetariaForm(forms.ModelForm):
    class Meta:
        model = CorrecaoMonetaria
        fields = ['valor', 'juros', 'multa', 'data_vencimento', 'data_pagamento']
