# Generated by Django 4.2.3 on 2023-10-29 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0012_alter_actividadpictogramas_orden'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividadpictogramas',
            name='orden',
            field=models.PositiveBigIntegerField(),
        ),
    ]