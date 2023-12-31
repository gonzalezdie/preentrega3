# Generated by Django 4.2.3 on 2023-08-13 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alquileres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoPropiedad', models.CharField(max_length=30)),
                ('ambientes', models.IntegerField()),
                ('localidad', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Asesores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=30)),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoPropiedad', models.CharField(max_length=30)),
                ('ambientes', models.IntegerField()),
                ('localidad', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
            ],
        ),
    ]
