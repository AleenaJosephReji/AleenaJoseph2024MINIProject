# Generated by Django 4.2.4 on 2023-09-17 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0030_memberprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='memberprofile',
            name='age',
        ),
        migrations.AddField(
            model_name='member',
            name='wardno',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
    ]
