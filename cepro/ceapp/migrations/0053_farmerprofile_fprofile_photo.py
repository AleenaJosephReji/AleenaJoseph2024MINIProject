# Generated by Django 4.2.4 on 2023-09-28 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0052_applycrop_is_approvedd'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmerprofile',
            name='fprofile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
    ]
