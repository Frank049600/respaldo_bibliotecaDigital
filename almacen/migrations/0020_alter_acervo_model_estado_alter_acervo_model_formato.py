# Generated by Django 5.0.4 on 2024-12-12 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0019_alter_acervo_model_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acervo_model',
            name='estado',
            field=models.CharField(blank=True, choices=[('Excelente', 'Excelente'), ('Bueno', 'Bueno'), ('Regular', 'Regular'), ('Malo', 'Malo')], default='Excelente', max_length=10, null=True, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='acervo_model',
            name='formato',
            field=models.CharField(blank=True, choices=[('Libro', 'Libro'), ('Disco', 'Disco')], default='Libro', max_length=6, null=True, verbose_name='formato'),
        ),
    ]
