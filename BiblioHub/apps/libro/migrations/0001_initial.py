# Generated by Django 4.2 on 2023-04-25 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('genero', '0001_initial'),
        ('autor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=100)),
                ('isbn', models.BigIntegerField()),
                ('borrado', models.BooleanField(default=False)),
                ('disponible', models.BooleanField(default=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='autor.autor')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='genero.genero')),
            ],
        ),
    ]
