# Generated by Django 4.2.4 on 2024-03-07 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0189_delete_machineryapply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machinery',
            name='user',
        ),
    ]
