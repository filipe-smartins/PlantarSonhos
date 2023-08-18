from django import forms


class CobrancaAdicionalForm(forms.Form):
    valor_hora = forms.DecimalField(label='Valor da Hora')
    hora_inicial = forms.TimeField(label='Hora Inicial', widget=forms.TimeInput(attrs={'placeholder': 'HH:MM'}))
    hora_final = forms.TimeField(label='Hora Final', widget=forms.TimeInput(attrs={'placeholder': 'HH:MM'}))
