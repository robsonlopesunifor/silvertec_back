# Generated by Django 2.2.3 on 2019-08-04 18:10

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computador', '0005_auto_20190804_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='computador',
            name='memoria_ram',
        ),
        migrations.AddField(
            model_name='computador',
            name='memoria_ram',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=2), size=None),
            preserve_default=False,
        ),
    ]
