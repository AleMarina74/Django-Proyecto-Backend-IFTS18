# Generated by Django 4.2 on 2023-06-05 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='disponible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='domicilio',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
