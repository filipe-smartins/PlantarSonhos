from django.shortcuts import render
from datetime import datetime, timedelta

from .forms import CobrancaAdicionalForm


def cobranca_adicional(request):
    total = None
    if request.method == 'POST':
        form = CobrancaAdicionalForm(request.POST)
        if form.is_valid():
            valor_hora = form.cleaned_data['valor_hora']
            hora_inicial = form.cleaned_data['hora_inicial']
            hora_final = form.cleaned_data['hora_final']

            inicio = datetime.combine(datetime.today(), hora_inicial)
            fim = datetime.combine(datetime.today(), hora_final)

            diff = fim - inicio

            print(diff)

            total_minutos = diff.total_seconds() / 60
            print(total_minutos)
            print(type(total_minutos))
            total = int(valor_hora) * (total_minutos / 60)
            print(valor_hora)
            print(type(int(valor_hora)))
    else:
        form = CobrancaAdicionalForm()

    context = {'form': form, 'total': total}
    return render(request, 'cobranca_adicional.html', context)
