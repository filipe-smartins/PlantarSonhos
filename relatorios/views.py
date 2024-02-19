from django.http import HttpResponse

from django.shortcuts import render
from django.db.models import Sum
from django.db.models import Max
from django.views import View
from financeiro.models import Transacao, Aluno
from django.utils import timezone
from datetime import timedelta

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


class RelatorioView(View):
    template_name = 'relatorio_recebimentos.html'

    def get(self, request, *args, **kwargs):

        # Alunos ativos que não efetuaram pagamento nos últimos 30 dias
        data_limite = timezone.now() - timedelta(days=30)

        transacoes_periodo = Transacao.objects.filter(
            data__gte=data_limite,
            descricao='MENSALIDADE'
        )

        alunos_em_atraso = Aluno.objects.filter(
            situacao='ATIVO'
        ).exclude(
        transacao__in=transacoes_periodo
        ).annotate(
            ultima_transacao=Max('transacao__data'),
            ultimo_valor=Max('transacao__valor'),
            ultima_situacao=Max('situacao')
        ).order_by('-ultima_transacao')

        # Adiciona um número sequencial aos alunos
        for i, aluno in enumerate(alunos_em_atraso, start=1):
            aluno.numero_sequencial = i

        # Alunos ativos que efetuaram pagamento nos últimos 30 dias
        data_limite = timezone.now() - timedelta(days=30)
        alunos_em_dia = Aluno.objects.filter(
            situacao='ATIVO',
            transacao__descricao='MENSALIDADE',
            transacao__data__gte=data_limite
        ).annotate(
            ultima_transacao=Max('transacao__data'),
            ultimo_valor=Max('transacao__valor'),
            ultima_situacao=Max('situacao')
        ).order_by('-ultima_transacao')

        # Adiciona um número sequencial aos alunos
        for i, aluno in enumerate(alunos_em_dia, start=1):
            aluno.numero_sequencial = i


        context = {
            'alunos_em_atraso': alunos_em_atraso,
            'alunos_em_dia': alunos_em_dia,
        }

        return render(request, self.template_name, context)


class RelatorioAlunos(View):
    template_name = 'relatorio_alunos.html'

    def get(self, request, *args, **kwargs):
        # Adicione um contador sequencial
        alunos = Aluno.objects.filter(transacao__descricao='MENSALIDADE').annotate(
            ultima_transacao=Max('transacao__data'),
            ultimo_valor=Max('transacao__valor'),
            ultima_situacao=Max('situacao')
        ).order_by('-ultima_transacao')

        # Adiciona um número sequencial aos alunos
        for i, aluno in enumerate(alunos, start=1):
            aluno.numero_sequencial = i

        context = {
            'alunos': alunos,
        }

        return render(request, self.template_name, context)
