from django.contrib import admin
from import_export.admin import ExportMixin
from .models import Aluno, Transacao
from .resources import TransacaoResource, AlunoResource

@admin.register(Aluno)
class AlunoAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = AlunoResource
    list_display = ('nome', 'responsavel', 'telefone', 'endereco')

@admin.register(Transacao)
class TransacaoAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = TransacaoResource
    list_display = ('data', 'tipo', 'valor', 'descricao', 'forma_pagamento', 'conta', 'comentarios', 'aluno')
