# Generated by Django 4.2.4 on 2024-02-06 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0135_sellapply_driver'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sell',
            name='driver',
        ),
    ]