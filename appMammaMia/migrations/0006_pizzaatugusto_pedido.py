# Generated by Django 4.2.7 on 2023-12-02 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appMammaMia', '0005_remove_ingrediente_pizzas'),
    ]

    operations = [
        migrations.CreateModel(
            name='PizzaATuGusto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingrediente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appMammaMia.ingrediente')),
                ('masa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appMammaMia.masa')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entrantes', models.CharField(max_length=100)),
                ('bebidas', models.CharField(max_length=100)),
                ('pizza', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='appMammaMia.pizza')),
                ('pizzaATuGusto', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='appMammaMia.pizzaatugusto')),
            ],
        ),
    ]
