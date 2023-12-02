# Generated by Django 4.2.7 on 2023-12-02 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMammaMia', '0006_pizzaatugusto_pedido'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bebida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Entrante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(upload_to='')),
            ],
        ),
        migrations.RenameField(
            model_name='reserva',
            old_name='nombre_persona',
            new_name='nombre',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='bebidas',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='entrantes',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='pizza',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='pizzaATuGusto',
        ),
        migrations.RemoveField(
            model_name='pizzaatugusto',
            name='ingrediente',
        ),
        migrations.AddField(
            model_name='pedido',
            name='bebidas',
            field=models.ManyToManyField(blank=True, to='appMammaMia.bebida'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='entrantes',
            field=models.ManyToManyField(blank=True, to='appMammaMia.entrante'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='pizza',
            field=models.ManyToManyField(blank=True, to='appMammaMia.pizza'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='pizzaATuGusto',
            field=models.ManyToManyField(blank=True, to='appMammaMia.pizzaatugusto'),
        ),
        migrations.AddField(
            model_name='pizzaatugusto',
            name='ingrediente',
            field=models.ManyToManyField(to='appMammaMia.ingrediente'),
        ),
    ]
