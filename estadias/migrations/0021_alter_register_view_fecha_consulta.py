# Generated by Django 5.0.4 on 2024-11-23 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estadias', '0020_alter_register_view_id_reporte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register_view',
            name='fecha_consulta',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de consulta'),
        ),
    ]
