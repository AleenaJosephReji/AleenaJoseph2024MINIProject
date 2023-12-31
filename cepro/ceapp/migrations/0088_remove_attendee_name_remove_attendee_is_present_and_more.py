# Generated by Django 4.2.4 on 2023-10-13 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0087_attendee_name_attendee_user_attendee_wardno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendee',
            name='Name',
        ),
        migrations.RemoveField(
            model_name='attendee',
            name='is_present',
        ),
        migrations.RemoveField(
            model_name='attendee',
            name='user',
        ),
        migrations.RemoveField(
            model_name='attendee',
            name='wardno',
        ),
        migrations.AddField(
            model_name='attendee',
            name='anna_attendance',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='attendee',
            name='annu_attendance',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='attendee',
            name='arya_attendance',
            field=models.BooleanField(default=False),
        ),
    ]
