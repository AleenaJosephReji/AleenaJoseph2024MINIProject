# Generated by Django 4.2.4 on 2024-03-12 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0204_machineryapplication_tcount'),
    ]

    operations = [
        migrations.AddField(
            model_name='machineryapplication',
            name='file_upload',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]