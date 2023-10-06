# Generated by Django 4.2.4 on 2023-10-06 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0066_meeting_last_edited_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crop',
            name='is_approved',
        ),
        migrations.AddField(
            model_name='applycrop',
            name='is_given',
            field=models.CharField(choices=[('given', 'Given'), ('notgiven', 'Notgiven')], default='notgiven', max_length=10),
        ),
    ]
