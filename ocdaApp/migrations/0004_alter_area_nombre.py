# Generated by Django 3.2.7 on 2021-10-03 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocdaApp', '0003_alter_area_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]