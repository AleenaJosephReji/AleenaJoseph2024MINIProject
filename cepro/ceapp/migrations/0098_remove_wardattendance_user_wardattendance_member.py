# Generated by Django 4.2.4 on 2023-10-19 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0097_remove_meeting_attendees_delete_attendee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wardattendance',
            name='user',
        ),
        migrations.AddField(
            model_name='wardattendance',
            name='member',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ceapp.member'),
        ),
    ]