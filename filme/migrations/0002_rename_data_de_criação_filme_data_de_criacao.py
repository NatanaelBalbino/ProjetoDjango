# Generated by Django 5.1.3 on 2024-11-20 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filme', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filme',
            old_name='data_de_criação',
            new_name='data_de_criacao',
        ),
    ]
