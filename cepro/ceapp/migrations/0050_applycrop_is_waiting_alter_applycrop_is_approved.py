# Generated by Django 4.2.4 on 2023-09-26 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0049_farmerprofile_file_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='applycrop',
            name='is_waiting',
            field=models.CharField(choices=[('waiting', 'waiting'), ('notwaiting', 'notwaiting')], default='waiting', max_length=10),
        ),
        migrations.AlterField(
            model_name='applycrop',
            name='is_approved',
            field=models.CharField(choices=[('approved', 'Approved'), ('rejected', 'Rejected'), ('pending', 'Pending')], default='pending', max_length=10),
        ),
    ]
