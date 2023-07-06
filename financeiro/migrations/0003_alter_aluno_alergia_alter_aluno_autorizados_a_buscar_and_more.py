# Generated by Django 4.2.3 on 2023-07-06 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0002_aluno_alter_transacao_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='alergia',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='autorizados_a_buscar',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='cpf_1',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='cpf_2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='endereco',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='fim_contrato',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='rg_1',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='rg_2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='telefone_1',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='telefone_2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]