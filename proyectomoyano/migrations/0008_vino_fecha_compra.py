# Generated by Django 4.2.6 on 2023-11-11 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectomoyano', '0007_vino_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='vino',
            name='fecha_compra',
            field=models.DateField(null=True),
        ),
    ]