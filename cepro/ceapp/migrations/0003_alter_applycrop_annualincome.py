# Generated by Django 4.2.4 on 2023-09-13 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0002_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applycrop',
            name='AnnualIncome',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]