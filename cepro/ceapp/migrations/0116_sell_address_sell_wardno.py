# Generated by Django 4.2.4 on 2024-02-02 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0115_sell_farmername'),
    ]

    operations = [
        migrations.AddField(
            model_name='sell',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sell',
            name='wardNo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]