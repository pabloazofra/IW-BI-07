# Generated by Django 5.0 on 2023-12-08 22:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMammaMia', '0024_remove_reserva_mesas_reserva_hora_reserva_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='fecha_y_hora',
        ),
        migrations.AddField(
            model_name='reserva',
            name='fecha_reserva',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
