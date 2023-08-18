from django.shortcuts import render
from .forms import CorrecaoMonetariaForm


def correcao_monetaria(request):
    instance = None
    if request.method == 'POST':
        form = CorrecaoMonetariaForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)

            atraso = (instance.data_pagamento - instance.data_vencimento).days

            valor_juros = instance.valor * (instance.juros/100)*atraso/30
            valor_multa = instance.valor * (instance.multa/100)

            valor_corrigido = instance.valor + valor_juros + valor_multa

            instance.atraso = atraso
            instance.valor_juros = valor_juros
            instance.valor_multa = valor_multa
            instance.valor_corrigido = valor_corrigido

            instance.save()
    else:
        form = CorrecaoMonetariaForm()

    context = {'form': form, 'instance': instance}
    return render(request, 'correcao_monetaria.html', context)
