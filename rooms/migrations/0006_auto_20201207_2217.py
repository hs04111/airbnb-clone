# Generated by Django 2.2.5 on 2020-12-07 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_auto_20201206_1517'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='adress',
            new_name='address',
        ),
    ]
