# Generated by Django 4.2.6 on 2023-11-14 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensajes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensaje',
            name='leido',
            field=models.BooleanField(default=False),
        ),
    ]