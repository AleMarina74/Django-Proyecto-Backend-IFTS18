# Generated by Django 4.2 on 2023-06-20 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('genero', '0002_alter_genero_nombre'),
        ('autor', '0003_alter_autor_nombre'),
        ('libro', '0006_alter_libro_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='libros', to='autor.autor', verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='genero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='libros', to='genero.genero', verbose_name='Genero'),
        ),
    ]
