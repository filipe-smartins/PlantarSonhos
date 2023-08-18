from django.db import models


class CorrecaoMonetaria(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    juros = models.DecimalField(max_digits=5, decimal_places=2)
    multa = models.DecimalField(max_digits=5, decimal_places=2)
    data_vencimento = models.DateField()
    data_pagamento = models.DateField()
    valor_corrigido = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
