# Generated by Django 3.2.7 on 2021-10-01 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionAlumnos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='curso',
            new_name='area',
        ),
    ]
