# Generated by Django 4.2.4 on 2023-10-13 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0083_remove_meeting_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
