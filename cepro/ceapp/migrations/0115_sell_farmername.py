# Generated by Django 4.2.4 on 2024-02-01 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0114_sell_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='sell',
            name='farmerName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]