# Generated by Django 4.2.4 on 2024-03-07 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0185_applicationmachinery_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='machinery',
            name='machinery_photo',
            field=models.ImageField(blank=True, null=True, upload_to='crop_photos/'),
        ),
    ]
