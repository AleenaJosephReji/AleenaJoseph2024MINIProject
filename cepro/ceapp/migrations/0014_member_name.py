# Generated by Django 4.2.4 on 2023-09-14 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0013_alter_applycrop_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='Name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
