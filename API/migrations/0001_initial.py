# Generated by Django 5.0.6 on 2024-05-29 13:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('nacionalidad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_usuario', models.IntegerField()),
                ('nif', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=100)),
                ('titulo', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=30)),
                ('editorial', models.CharField(max_length=60)),
                ('num_pags', models.PositiveSmallIntegerField()),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.autor')),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_prestamo', models.DateTimeField()),
                ('fecha_devolucion', models.DateTimeField()),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.libro')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.usuario')),
            ],
        ),
    ]