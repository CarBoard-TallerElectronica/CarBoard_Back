# Generated by Django 3.2.6 on 2023-10-26 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nodo', '0001_initial'),
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Measurements',
            new_name='Measurement',
        ),
    ]