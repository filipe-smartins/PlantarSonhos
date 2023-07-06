from django.db import models
from django.utils import timezone


class Aluno(models.Model):

    INTEGRAL = 'INTEGRAL'
    PARCIAL_MANHA = 'PARCIAL_MANHA'
    PARCIAL_TARDE = 'PARCIAL_TARDE'
    PERSOLIZADO = 'PERSOLIZADO'

    MODALIDADE_CHOICE = [
        (INTEGRAL, 'INTEGRAL'),
        (PARCIAL_MANHA, 'PARCIAL_MANHA'),
        (PARCIAL_TARDE, 'PARCIAL_TARDE'),
        (PERSOLIZADO, 'PERSOLIZADO'),
    ]

    ATIVO = 'ATIVO'
    INATIVO = 'INATIVO'

    SITUACAO_CHOICE = [
        (ATIVO, 'ATIVO'),
        (INATIVO, 'INATIVO'),
    ]

    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    alergia = models.CharField(max_length=200, blank=True, null=True)
    responsavel_1 = models.CharField(max_length=100)
    telefone_1 = models.CharField(max_length=20, blank=True, null=True)
    cpf_1 = models.CharField(max_length=20, blank=True, null=True)
    rg_1 = models.CharField(max_length=20, blank=True, null=True)
    responsavel_2 = models.CharField(max_length=100)
    telefone_2 = models.CharField(max_length=20, blank=True, null=True)
    cpf_2 = models.CharField(max_length=20, blank=True, null=True)
    rg_2 = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.CharField(max_length=200, blank=True, null=True)
    modalidade = models.CharField(max_length=50, choices=MODALIDADE_CHOICE)
    autorizados_a_buscar = models.CharField(max_length=200, blank=True, null=True)
    inicio_contrato = models.DateField()
    fim_contrato = models.DateField(blank=True, null=True)
    situacao = models.CharField(max_length=50, choices=SITUACAO_CHOICE)


    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Alunos'


class Transacao(models.Model):
    RECEITA = 'RECEITA'
    DESPESA = 'DESPESA'
    RESERVA = 'RESERVA'
    DISTRIBUICAO = 'DISTRIBUICAO'
    TRANSFERENCIA = 'TRANSFERENCIA'

    TIPOS_CHOICE = [
        (RECEITA, 'RECEITA'),
        (DESPESA, 'DESPESA'),
        (RESERVA, 'RESERVA'),
        (DISTRIBUICAO, 'DISTRIBUICAO'),
        (TRANSFERENCIA, 'TRANSFERENCIA'),
    ]

    MENSALIDADE = 'MENSALIDADE'
    ALUGUEL = 'ALUGUEL'
    COPASA = 'COPASA'
    MATERIAL = 'MATERIAL'
    FUNCIONARIOS = 'FUNCIONARIOS'
    COMPRA_EQUIPAMENTOS = 'COMPRA_EQUIPAMENTOS'
    REFORMAS_MELHORIAS = 'REFORMAS_MELHORIAS'
    PRODUTOS_LIMPEZA = 'PRODUTOS_LIMPEZA'
    OUTRAS_DESPESAS = 'OUTRAS_DESPESAS'
    OUTRAS_RECEITAS = 'OUTRAS_RECEITAS'
    DISTRIBUICAO_LUCROS = 'DISTRIBUICAO_LUCROS'
    RESERVA_CAIXA = 'RESERVA_CAIXA'

    DESCRICAO_CHOICE = [
        (MENSALIDADE, 'MENSALIDADE'),
        (ALUGUEL, 'ALUGUEL'),
        (COPASA, 'COPASA'),
        (MATERIAL, 'MATERIAL'),
        (FUNCIONARIOS, 'FUNCIONARIOS'),
        (COMPRA_EQUIPAMENTOS, 'COMPRA_EQUIPAMENTOS'),
        (REFORMAS_MELHORIAS, 'REFORMAS_MELHORIAS'),
        (PRODUTOS_LIMPEZA, 'PRODUTOS_LIMPEZA'),
        (OUTRAS_DESPESAS, 'OUTRAS_DESPESAS'),
        (OUTRAS_RECEITAS, 'OUTRAS_RECEITAS'),
        (DISTRIBUICAO_LUCROS, 'DISTRIBUICAO_LUCROS'),
        (RESERVA_CAIXA, 'RESERVA_CAIXA'),
    ]

    DINHEIRO = 'DINHEIRO'
    CONTA_BANCARIA = 'CONTA_BANCARIA'
    RESERVA_CAIXA = 'RESERVA_CAIXA'

    TIPOS_PGTO = [
        (DINHEIRO, 'DINHEIRO'),
        (CONTA_BANCARIA, 'CONTA_BANCARIA'),
        (RESERVA_CAIXA, 'RESERVA_CAIXA'),
    ]

    DAYANE = 'DAYANE'
    POLYANA = 'POLYANA'
    RESERVA = 'RESERVA'
    MEI = 'MEI'
    CAIXA = 'CAIXA'


    CONTAS_CHOICE = [
        (DAYANE, 'DAYANE'),
        (POLYANA, 'POLYANA'),
        (RESERVA, 'RESERVA'),
        (MEI, 'MEI'),
        (CAIXA, 'CAIXA'),
    ]

    data = models.DateField(default=timezone.now)
    tipo = models.CharField(max_length=50, choices=TIPOS_CHOICE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=50, choices=DESCRICAO_CHOICE)
    forma_pagamento = models.CharField(max_length=100, choices=TIPOS_PGTO)
    conta = models.CharField(max_length=100, choices=CONTAS_CHOICE)
    comentarios = models.CharField(max_length=200)
    aluno = models.ForeignKey(Aluno, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Transação - {self.tipo}"

    class Meta:
        verbose_name_plural = 'Transações'

