# Generated by Django 4.2 on 2023-06-20 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestamo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestamo',
            name='devolucion',
            field=models.BooleanField(default=False),
        ),
    ]
