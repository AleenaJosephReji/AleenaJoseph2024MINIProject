# Generated by Django 4.2.4 on 2023-10-01 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0055_crop_given'),
    ]

    operations = [
        migrations.AddField(
            model_name='applycrop',
            name='land',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
