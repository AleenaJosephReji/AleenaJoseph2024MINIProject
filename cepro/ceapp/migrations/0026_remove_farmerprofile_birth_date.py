# Generated by Django 4.2.4 on 2023-09-17 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0025_alter_farmerprofile_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farmerprofile',
            name='birth_date',
        ),
    ]
