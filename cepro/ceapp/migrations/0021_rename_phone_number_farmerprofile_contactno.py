# Generated by Django 4.2.4 on 2023-09-15 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0020_rename_ward_farmerprofile_wardno'),
    ]

    operations = [
        migrations.RenameField(
            model_name='farmerprofile',
            old_name='phone_number',
            new_name='contactNo',
        ),
    ]
