# Generated by Django 4.2.4 on 2023-10-05 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0063_member_institution'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crop',
            name='given',
        ),
        migrations.AddField(
            model_name='crop',
            name='is_approved',
            field=models.CharField(choices=[('approved', 'Approved'), ('pending', 'Pending')], default='pending', max_length=10),
        ),
    ]
