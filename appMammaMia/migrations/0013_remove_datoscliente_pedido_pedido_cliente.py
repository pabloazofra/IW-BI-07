# Generated by Django 4.2.7 on 2023-12-03 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appMammaMia', '0012_alter_datoscliente_telefono'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datoscliente',
            name='pedido',
        ),
        migrations.AddField(
            model_name='pedido',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='appMammaMia.datoscliente'),
        ),
    ]
