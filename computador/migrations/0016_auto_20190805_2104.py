# Generated by Django 2.2.3 on 2019-08-05 21:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('computador', '0015_computador_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computador',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
