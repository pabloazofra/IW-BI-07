# Generated by Django 4.2.7 on 2023-12-08 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMammaMia', '0026_pedido_preciototal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='precioTotal',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]