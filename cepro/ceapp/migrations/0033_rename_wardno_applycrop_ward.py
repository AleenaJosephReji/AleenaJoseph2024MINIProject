# Generated by Django 4.2.4 on 2023-09-17 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0032_applycrop_file_upload'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applycrop',
            old_name='wardNo',
            new_name='ward',
        ),
    ]
