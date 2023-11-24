# Generated by Django 4.2.7 on 2023-11-20 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0019_rename_frases_frase'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividadordenaroracion',
            name='oracion',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='tipo',
            field=models.CharField(choices=[('PIC', 'Pictograma'), ('DIB', 'Dibujo'), ('MEM', 'Memoria'), ('ORD', 'Ordenar Oración')]),
        ),
        migrations.AlterField(
            model_name='modulo',
            name='tipo',
            field=models.CharField(choices=[('PIC', 'Pictograma'), ('DIB', 'Dibujo'), ('MEM', 'Memoria'), ('ORD', 'Ordenar Oración')]),
        ),
    ]
