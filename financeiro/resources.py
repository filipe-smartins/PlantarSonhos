from import_export import resources
from .models import Transacao, Aluno


class AlunoResource(resources.ModelResource):
    class Meta:
        model = Aluno
        fields = ('nome', 'responsavel', 'telefone', 'endereco')


class TransacaoResource(resources.ModelResource):
    class Meta:
        model = Transacao
        fields = ('data', 'tipo', 'valor', 'descricao', 'forma_pagamento', 'conta', 'comentarios', 'aluno')
