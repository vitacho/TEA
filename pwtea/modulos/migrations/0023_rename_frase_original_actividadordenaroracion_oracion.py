# Generated by Django 4.2.7 on 2023-11-20 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0022_rename_oracionn_actividadordenaroracion_frase_original'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actividadordenaroracion',
            old_name='frase_original',
            new_name='oracion',
        ),
    ]
