# Generated by Django 4.2.3 on 2023-10-29 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0010_modulo_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actividadpictogramas',
            name='nombre_pictograma',
        ),
        migrations.AlterField(
            model_name='actividad',
            name='tipo',
            field=models.CharField(choices=[('PIC', 'Pictograma'), ('DIB', 'Dibujo'), ('MEM', 'Memoria')]),
        ),
        migrations.AlterField(
            model_name='modulo',
            name='tipo',
            field=models.CharField(choices=[('PIC', 'Pictograma'), ('DIB', 'Dibujo'), ('MEM', 'Memoria')]),
        ),
    ]