# Generated by Django 4.2.4 on 2023-10-06 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0065_meeting'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='last_edited_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
