# Generated by Django 4.2.4 on 2024-03-06 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0181_remove_machinery_applied_by_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machineryapply',
            name='applied_by',
        ),
        migrations.RemoveField(
            model_name='machineryapply',
            name='apply_date',
        ),
        migrations.RemoveField(
            model_name='machineryapply',
            name='available',
        ),
        migrations.RemoveField(
            model_name='machineryapply',
            name='farmerName',
        ),
        migrations.AddField(
            model_name='machinery',
            name='applied_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applied_machines', to='ceapp.farmerprofile'),
        ),
        migrations.AddField(
            model_name='machinery',
            name='apply_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='machinery',
            name='available',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='machinery',
            name='farmerName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
