# Generated by Django 4.2.6 on 2023-11-09 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectomoyano', '0006_rename_consulta_contacto_consulta_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vino',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
    ]
