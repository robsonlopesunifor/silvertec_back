# Generated by Django 2.2.3 on 2019-08-04 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('computador', '0003_auto_20190804_0237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computador',
            name='placa_video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='computador.PlacaVideo'),
        ),
    ]
