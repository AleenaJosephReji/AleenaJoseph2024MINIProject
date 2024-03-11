# Generated by Django 4.2.4 on 2024-03-11 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0201_machineryapplication_total_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machineryapplication',
            name='machinery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='ceapp.addmachinery'),
        ),
    ]
