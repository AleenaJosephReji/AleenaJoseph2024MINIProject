# Generated by Django 4.2.4 on 2024-03-16 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0209_machineryapplication_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='machinerytcount',
            name='mname',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]
