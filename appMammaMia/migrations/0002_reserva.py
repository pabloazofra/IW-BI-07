# Generated by Django 4.2.7 on 2023-11-30 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMammaMia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_persona', models.CharField(max_length=100)),
                ('telefono', models.IntegerField(max_length=9)),
            ],
        ),
    ]
