# Generated by Django 4.2.4 on 2023-10-04 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0059_member_aemail'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='date_of_birth',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
