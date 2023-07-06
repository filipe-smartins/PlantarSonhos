from django.contrib import admin
from import_export.admin import ExportMixin
from .models import Aluno, Transacao
from .resources import TransacaoResource, AlunoResource

@admin.register(Aluno)
class AlunoAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = AlunoResource
    list_display = ('nome', 'data_nascimento', 'alergia', 'responsavel_1', 'telefone_1', 'cpf_1', 'rg_1', 'responsavel_2', 'telefone_2', 'cpf_2', 'rg_2', 'endereco', 'modalidade', 'autorizados_a_buscar', 'inicio_contrato', 'fim_contrato', 'situacao')

@admin.register(Transacao)
class TransacaoAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = TransacaoResource
    list_display = ('data', 'tipo', 'valor', 'descricao', 'forma_pagamento', 'conta', 'comentarios', 'aluno')
