# Generated by Django 4.2.4 on 2023-10-09 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0070_meeting_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='attendance',
            field=models.BooleanField(default=False),
        ),
    ]
