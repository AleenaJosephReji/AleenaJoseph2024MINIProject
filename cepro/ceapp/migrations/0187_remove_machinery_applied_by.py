# Generated by Django 4.2.4 on 2024-03-07 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0186_machinery_machinery_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machinery',
            name='applied_by',
        ),
    ]
