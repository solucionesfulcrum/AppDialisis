# Generated by Django 3.1.1 on 2022-03-01 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DP', '0010_usuario_primsesion'),
    ]

    operations = [
        migrations.AddField(
            model_name='dp_diario',
            name='pres_art_diast',
            field=models.IntegerField(default=21),
            preserve_default=False,
        ),
    ]
