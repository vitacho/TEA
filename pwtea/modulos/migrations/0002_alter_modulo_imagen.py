# Generated by Django 4.2.3 on 2023-10-20 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulo',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='modulos_imagen/'),
        ),
    ]
