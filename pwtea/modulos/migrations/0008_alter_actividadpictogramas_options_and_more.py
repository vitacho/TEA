# Generated by Django 4.2.3 on 2023-10-23 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0007_actividadpictogramas_orden'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actividadpictogramas',
            options={'ordering': ['categoria', 'orden']},
        ),
        migrations.AlterField(
            model_name='actividadpictogramas',
            name='orden',
            field=models.PositiveBigIntegerField(),
        ),
    ]
