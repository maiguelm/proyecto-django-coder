# Generated by Django 4.2.6 on 2023-10-29 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectomoyano', '0002_vino_delete_paleta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=30)),
                ('Mail', models.CharField(max_length=30)),
                ('Telefono', models.IntegerField()),
                ('Consulta', models.CharField(max_length=150)),
            ],
        ),
    ]