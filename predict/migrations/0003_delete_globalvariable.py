# Generated by Django 4.1 on 2023-07-07 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0002_alter_globalvariable_value'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GlobalVariable',
        ),
    ]