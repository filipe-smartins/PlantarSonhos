from import_export import resources
from .models import Transacao, Aluno


class AlunoResource(resources.ModelResource):
    class Meta:
        model = Aluno
        fields = ('nome', 'data_nascimento', 'alergia', 'responsavel_1', 'telefone_1', 'cpf_1', 'rg_1', 'responsavel_2', 'telefone_2', 'cpf_2', 'rg_2', 'endereco', 'modalidade', 'autorizados_a_buscar', 'inicio_contrato', 'fim_contrato', 'situacao')


class TransacaoResource(resources.ModelResource):
    class Meta:
        model = Transacao
        fields = ('data', 'tipo', 'valor', 'descricao', 'forma_pagamento', 'conta', 'comentarios', 'aluno')
