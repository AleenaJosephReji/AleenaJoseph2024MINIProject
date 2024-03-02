# Generated by Django 4.2.4 on 2024-03-02 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0159_mleave'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mleave',
            name='meeting_date',
        ),
        migrations.RemoveField(
            model_name='mleave',
            name='meeting_time',
        ),
        migrations.RemoveField(
            model_name='mleave',
            name='meeting_venue',
        ),
        migrations.AddField(
            model_name='mleave',
            name='meeting',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ceapp.meeting'),
        ),
        migrations.AddField(
            model_name='mleave',
            name='member',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ceapp.member'),
        ),
        migrations.AddField(
            model_name='mleave',
            name='wardattendance',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ceapp.wardattendance'),
        ),
    ]
