# Generated by Django 4.2.7 on 2023-12-07 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMammaMia', '0020_alter_bebida_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bebida',
            name='descripcion',
        ),
        migrations.AlterField(
            model_name='ingrediente',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
