# Generated by Django 4.2 on 2023-04-11 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0002_rename_usuario_tareas_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tareas',
            name='fecha_termino',
            field=models.DateTimeField(null=True),
        ),
    ]