# Generated by Django 4.2.7 on 2023-11-22 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0025_alter_palabra_texto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividadordenaroracion',
            name='palabras',
            field=models.ManyToManyField(blank=True, null=True, to='modulos.palabra'),
        ),
    ]
