# Generated by Django 4.2.4 on 2023-10-03 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0056_applycrop_land'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
