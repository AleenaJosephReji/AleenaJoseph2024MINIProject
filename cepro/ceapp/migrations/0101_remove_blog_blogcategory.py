# Generated by Django 4.2.4 on 2024-01-16 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0100_crop_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='blogcategory',
        ),
    ]
