# Generated by Django 3.2.7 on 2021-10-03 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocdaApp', '0004_alter_area_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='dni',
            field=models.IntegerField(default=0, max_length=8),
        ),
        migrations.AlterField(
            model_name='docente',
            name='dni',
            field=models.IntegerField(default=0, max_length=8),
        ),
    ]
