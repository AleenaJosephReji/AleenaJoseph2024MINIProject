# Generated by Django 4.2.4 on 2023-09-24 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0044_alter_crop_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='crop',
            name='crop_photo',
            field=models.ImageField(blank=True, null=True, upload_to='crop_photo/'),
        ),
    ]
