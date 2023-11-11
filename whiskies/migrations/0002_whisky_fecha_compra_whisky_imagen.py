# Generated by Django 4.2.6 on 2023-11-11 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whiskies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='whisky',
            name='fecha_compra',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='whisky',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
    ]
