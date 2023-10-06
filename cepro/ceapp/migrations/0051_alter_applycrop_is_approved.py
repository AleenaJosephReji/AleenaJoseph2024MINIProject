# Generated by Django 4.2.4 on 2023-09-26 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0050_applycrop_is_waiting_alter_applycrop_is_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applycrop',
            name='is_approved',
            field=models.CharField(choices=[('approved', 'Approved'), ('rejected', 'Rejected'), ('pending', 'Pending'), ('waiting', 'waiting')], default='pending', max_length=10),
        ),
    ]