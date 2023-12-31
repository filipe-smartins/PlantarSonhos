# Generated by Django 4.2.3 on 2023-07-06 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('tipo', models.CharField(max_length=100)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descricao', models.CharField(max_length=100)),
                ('forma_pagamento', models.CharField(max_length=100)),
                ('conta', models.CharField(max_length=100)),
                ('referencia', models.CharField(max_length=100)),
                ('comentarios', models.CharField(max_length=200)),
            ],
        ),
    ]
