# Generated by Django 4.2 on 2023-04-10 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tareas',
            old_name='usuario',
            new_name='user',
        ),
    ]