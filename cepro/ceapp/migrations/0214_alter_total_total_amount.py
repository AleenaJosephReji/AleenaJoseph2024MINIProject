# Generated by Django 4.2.4 on 2024-03-27 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0213_alter_sellapply_total_amount_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='total',
            name='total_amount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]
