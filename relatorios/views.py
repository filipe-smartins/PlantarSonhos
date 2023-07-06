from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

from django.shortcuts import render
from django.db.models import Sum
from financeiro.models import Transacao


def relatorios(request):
    total_conta_polyana = Transacao.objects.filter(forma_pagamento='CONTA_BANCARIA', conta='POLYANA').aggregate(total=Sum('valor'))['total']
    total_conta_dayane = Transacao.objects.filter(forma_pagamento='CONTA_BANCARIA', conta='DAYANE').aggregate(total=Sum('valor'))['total']
    total_conta_mei = Transacao.objects.filter(forma_pagamento='CONTA_BANCARIA', conta='MEI').aggregate(total=Sum('valor'))['total']
    total_conta_caixa = Transacao.objects.filter(forma_pagamento='DINHEIRO', conta='CAIXA').aggregate(total=Sum('valor'))['total']
    total_conta_reserva = Transacao.objects.filter(forma_pagamento='RESERVA_CAIXA', conta='RESERVA').aggregate(total=Sum('valor'))['total']
    total = Transacao.objects.aggregate(total=Sum('valor'))['total']

    total_conta_polyana = 0 if total_conta_polyana==None else float(total_conta_polyana)
    total_conta_dayane = 0 if total_conta_dayane == None else float(total_conta_dayane)
    total_conta_mei = 0 if total_conta_mei == None else float(total_conta_mei)
    total_conta_caixa = 0 if total_conta_caixa == None else float(total_conta_caixa)
    total_conta_reserva = 0 if total_conta_reserva == None else float(total_conta_reserva)
    total = 0 if total == None else float(total)

    context = {
        'total_conta_polyana': total_conta_polyana,
        'total_conta_dayane': total_conta_dayane,
        'total_conta_mei': total_conta_mei,
        'total_conta_caixa': total_conta_caixa,
        'total_conta_reserva': total_conta_reserva,
        'total': total,
    }

    return render(request, 'relatorios.html', context)

