# Generated by Django 2.2.3 on 2019-08-04 19:38

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computador', '0013_auto_20190804_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computador',
            name='memoria_ram',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=2), size=None),
        ),
    ]
