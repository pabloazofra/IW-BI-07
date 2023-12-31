# Generated by Django 4.2.7 on 2023-12-03 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMammaMia', '0007_bebida_entrante_rename_nombre_persona_reserva_nombre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingrediente',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='ingredientes/'),
        ),
        migrations.CreateModel(
            name='DatosCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCliente', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=50)),
                ('direccion', models.TextField()),
                ('pedido', models.ManyToManyField(to='appMammaMia.pedido')),
            ],
        ),
    ]
