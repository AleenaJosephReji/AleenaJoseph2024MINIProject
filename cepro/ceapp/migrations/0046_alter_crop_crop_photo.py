# Generated by Django 4.2.4 on 2023-09-24 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0045_crop_crop_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crop',
            name='crop_photo',
            field=models.ImageField(blank=True, null=True, upload_to='crop_photos/'),
        ),
    ]