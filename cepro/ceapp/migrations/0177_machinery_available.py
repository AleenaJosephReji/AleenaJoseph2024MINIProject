# Generated by Django 4.2.4 on 2024-03-06 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0176_machinery_days'),
    ]

    operations = [
        migrations.AddField(
            model_name='machinery',
            name='available',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
    ]