# Generated by Django 4.2.3 on 2023-10-22 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0003_alter_categoria_imagen_alter_modulo_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='modulo',
            name='tipo',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]