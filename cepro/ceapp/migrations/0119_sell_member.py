# Generated by Django 4.2.4 on 2024-02-02 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0118_sell_is_accept'),
    ]

    operations = [
        migrations.AddField(
            model_name='sell',
            name='member',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ceapp.member'),
        ),
    ]
