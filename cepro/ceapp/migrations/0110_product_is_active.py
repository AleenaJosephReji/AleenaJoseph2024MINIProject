# Generated by Django 4.2.4 on 2024-01-29 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0109_alter_service_serviceimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
