# Generated by Django 2.2.3 on 2019-08-04 18:52

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computador', '0009_computador_memoria_ram'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computador',
            name='memoria_ram',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), size=2), default=[0, 0], size=None),
        ),
    ]
