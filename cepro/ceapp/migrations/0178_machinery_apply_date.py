# Generated by Django 4.2.4 on 2024-03-06 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0177_machinery_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='machinery',
            name='apply_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
