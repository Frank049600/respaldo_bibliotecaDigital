# Generated by Django 5.0.4 on 2024-11-23 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_catalogo',
            name='tipoP',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
