# Generated by Django 5.1.3 on 2024-11-25 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filme', '0002_rename_data_de_criação_filme_data_de_criacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='categoria',
            field=models.CharField(choices=[('ANALISES', 'Análises'), ('MUSICA', 'Música'), ('PROGRAMACAO', 'Programação'), ('EXERCICIOS', 'Exercícios')], max_length=15),
        ),
    ]
