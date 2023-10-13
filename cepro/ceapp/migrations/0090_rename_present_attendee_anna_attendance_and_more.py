# Generated by Django 4.2.4 on 2023-10-13 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0089_rename_anna_attendance_attendee_present_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendee',
            old_name='present',
            new_name='anna_attendance',
        ),
        migrations.RemoveField(
            model_name='attendee',
            name='name',
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
