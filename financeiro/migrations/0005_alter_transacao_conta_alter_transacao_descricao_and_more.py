# Generated by Django 4.2.3 on 2023-07-06 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0004_aluno_transacao_aluno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='conta',
            field=models.CharField(choices=[('DAYANE', 'DAYANE'), ('POLYANA', 'POLYANA'), ('CONTA', 'CONTA'), ('MEI', 'MEI'), ('CAIXA', 'CAIXA')], max_length=100),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='descricao',
            field=models.CharField(choices=[('MENSALIDADE', 'MENSALIDADE'), ('ALUGUEL', 'ALUGUEL'), ('COPASA', 'COPASA'), ('MATERIAL', 'MATERIAL'), ('FUNCIONARIOS', 'FUNCIONARIOS'), ('COMPRA_EQUIPAMENTOS', 'COMPRA_EQUIPAMENTOS'), ('REFORMAS_MELHORIAS', 'REFORMAS_MELHORIAS'), ('PRODUTOS_LIMPEZA', 'PRODUTOS_LIMPEZA'), ('OUTRAS_DESPESAS', 'OUTRAS_DESPESAS'), ('OUTRAS_RECEITAS', 'OUTRAS_RECEITAS'), ('DISTRIBUICAO_LUCROS', 'DISTRIBUICAO_LUCROS'), ('RESERVA_CAIXA', 'RESERVA_CAIXA')], max_length=50),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='forma_pagamento',
            field=models.CharField(choices=[('DINHEIRO', 'DINHEIRO'), ('CARTAO_CREDITO', 'CARTAO_CREDITO'), ('CONTA_BANCARIA', 'CONTA_BANCARIA'), ('RESERVA_CAIXA', 'RESERVA_CAIXA')], max_length=100),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='tipo',
            field=models.CharField(choices=[('RECEITA', 'RECEITA'), ('DESPESA', 'DESPESA'), ('RESERVA', 'RESERVA'), ('DISTRIBUICAO', 'DISTRIBUICAO'), ('TRANSFERENCIA', 'TRANSFERENCIA')], max_length=50),
        ),
    ]
