# Generated by Django 4.2.4 on 2023-09-15 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0015_remove_crop_available_remove_crop_not_available_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='crop',
            name='count',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
