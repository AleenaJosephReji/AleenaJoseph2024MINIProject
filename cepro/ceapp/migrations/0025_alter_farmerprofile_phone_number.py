# Generated by Django 4.2.4 on 2023-09-15 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0024_alter_farmerprofile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmerprofile',
            name='phone_number',
            field=models.IntegerField(blank=True, max_length=12, null=True),
        ),
    ]
