# Generated by Django 4.2.4 on 2024-03-27 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0215_total_total_amount_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='total',
            name='total_amount_new',
        ),
    ]
