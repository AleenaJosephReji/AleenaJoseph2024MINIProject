# Generated by Django 4.2.4 on 2024-03-04 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0169_total_farmername'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='total',
            name='sell',
        ),
        migrations.RemoveField(
            model_name='total',
            name='sellapply',
        ),
        migrations.AlterField(
            model_name='total',
            name='total_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
