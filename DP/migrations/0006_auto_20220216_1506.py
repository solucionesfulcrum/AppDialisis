# Generated by Django 3.1.1 on 2022-02-16 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DP', '0005_auto_20220216_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examenlaboratorio',
            name='actividad',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='examenlaboratorio',
            name='categoria_resul',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='examenlaboratorio',
            name='fecha_atencion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='examenlaboratorio',
            name='fecha_cita',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='examenlaboratorio',
            name='informe_resultado',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='examenlaboratorio',
            name='observresultado',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='examenlaboratorio',
            name='subactividad',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='examenlaboratorio',
            name='unidadvalor',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
