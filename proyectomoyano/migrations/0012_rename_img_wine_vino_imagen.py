# Generated by Django 4.2.6 on 2023-11-12 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectomoyano', '0011_rename_imagen_vino_img_wine'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vino',
            old_name='img_wine',
            new_name='imagen',
        ),
    ]