# Generated by Django 4.2.4 on 2023-10-04 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0058_member_amob'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='aemail',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
