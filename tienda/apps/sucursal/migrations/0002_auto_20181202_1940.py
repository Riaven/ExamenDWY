# Generated by Django 2.1.3 on 2018-12-02 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sucursal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ciudad',
            old_name='region',
            new_name='comuna',
        ),
    ]
