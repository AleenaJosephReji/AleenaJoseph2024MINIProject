# Generated by Django 4.2.4 on 2023-09-17 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0031_remove_member_date_of_birth_remove_memberprofile_age_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='applycrop',
            name='file_upload',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
