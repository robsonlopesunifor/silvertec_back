# Generated by Django 2.2.3 on 2019-08-05 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('computador', '0016_auto_20190805_2104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='computador',
            name='cliente',
        ),
    ]
