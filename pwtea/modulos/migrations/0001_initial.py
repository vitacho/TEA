# Generated by Django 4.2.7 on 2023-12-29 09:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=250)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('tipo', models.CharField(choices=[('PIC', 'Pictograma'), ('DIB', 'Dibujo'), ('MEM', 'Memoria'), ('ORD', 'Ordenar Oración')])),
                ('activo', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=250)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(upload_to='modulos_imagen/')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('activo', models.BooleanField(default=True)),
                ('tipo', models.CharField(choices=[('PIC', 'Pictograma'), ('DIB', 'Dibujo'), ('MEM', 'Memoria'), ('ORD', 'Ordenar Oración')])),
            ],
        ),
        migrations.CreateModel(
            name='Ninio',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=250)),
                ('apellido', models.CharField(max_length=250)),
                ('fecha_nacimiento', models.DateField()),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=12)),
                ('grado_tea', models.CharField(choices=[('G1', 'Grado 1'), ('G2', 'Grado 2'), ('G3', 'Grado 3')], max_length=25)),
                ('activo', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Palabra',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('texto', models.CharField(max_length=250, unique=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='frases_imagen/')),
            ],
        ),
        migrations.CreateModel(
            name='ActividadComunicacion',
            fields=[
                ('actividad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='modulos.actividad')),
                ('dato', models.CharField(max_length=250)),
            ],
            bases=('modulos.actividad',),
        ),
        migrations.CreateModel(
            name='ActividadDibujo',
            fields=[
                ('actividad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='modulos.actividad')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='actividad_imagen/')),
            ],
            bases=('modulos.actividad',),
        ),
        migrations.CreateModel(
            name='ActividadEscritura',
            fields=[
                ('actividad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='modulos.actividad')),
                ('dato', models.CharField(max_length=250)),
            ],
            bases=('modulos.actividad',),
        ),
        migrations.CreateModel(
            name='ActividadFiguraFondo',
            fields=[
                ('actividad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='modulos.actividad')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='actividad_imagen/')),
            ],
            bases=('modulos.actividad',),
        ),
        migrations.CreateModel(
            name='ActividadGramaticaOrtografia',
            fields=[
                ('actividad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='modulos.actividad')),
                ('dato', models.CharField(max_length=250)),
            ],
            bases=('modulos.actividad',),
        ),
        migrations.CreateModel(
            name='ActividadMemoria',
            fields=[
                ('actividad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='modulos.actividad')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='actividad_imagen/')),
            ],
            bases=('modulos.actividad',),
        ),
        migrations.CreateModel(
            name='ActividadPercepcion',
            fields=[
                ('actividad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='modulos.actividad')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='actividad_imagen/')),
            ],
            bases=('modulos.actividad',),
        ),
        migrations.CreateModel(
            name='ActividadPictogramas',
            fields=[
                ('actividad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='modulos.actividad')),
                ('imagen_pictograma', models.ImageField(blank=True, null=True, upload_to='actividad_imagen/')),
                ('orden', models.PositiveBigIntegerField(blank=True, null=True)),
            ],
            bases=('modulos.actividad',),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('email', models.EmailField(max_length=254, unique=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('telefono', models.CharField(blank=True, max_length=10, null=True)),
                ('tipo_cuenta', models.CharField(choices=[('A', 'Administrador'), ('p', 'Padres'), ('E', 'Especialista'), ('D', 'Docente')], default='p', max_length=1)),
                ('activo', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('ninio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='modulos.ninio')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ResulatadosActividad',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('tiempoenresolver', models.IntegerField()),
                ('actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulos.actividad')),
                ('ninio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulos.ninio')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=250)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(upload_to='cateoria_imagen/')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('activo', models.BooleanField(default=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('modulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulos.modulo')),
            ],
        ),
        migrations.AddField(
            model_name='actividad',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulos.categoria'),
        ),
        migrations.CreateModel(
            name='ActividadOrdenarOracion',
            fields=[
                ('actividad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='modulos.actividad')),
                ('oracion', models.CharField(blank=True, max_length=250, null=True)),
                ('palabras', models.ManyToManyField(blank=True, to='modulos.palabra')),
            ],
            bases=('modulos.actividad',),
        ),
    ]
