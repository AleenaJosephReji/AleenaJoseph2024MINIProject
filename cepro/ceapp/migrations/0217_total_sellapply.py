# Generated by Django 4.2.4 on 2024-03-27 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0216_remove_total_total_amount_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='total',
            name='sellapply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ceapp.sellapply'),
        ),
    ]
