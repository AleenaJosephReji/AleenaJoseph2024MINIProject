# Generated by Django 4.2.4 on 2024-03-04 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0166_sellapply_total_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellapply',
            name='total_cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
