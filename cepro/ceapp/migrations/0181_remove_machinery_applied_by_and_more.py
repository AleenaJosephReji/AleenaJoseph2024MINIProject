# Generated by Django 4.2.4 on 2024-03-06 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0180_machinery_applied_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machinery',
            name='applied_by',
        ),
        migrations.RemoveField(
            model_name='machinery',
            name='apply_date',
        ),
        migrations.RemoveField(
            model_name='machinery',
            name='available',
        ),
        migrations.RemoveField(
            model_name='machinery',
            name='farmerName',
        ),
        migrations.CreateModel(
            name='MachineryApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.IntegerField(blank=True, max_length=100, null=True)),
                ('apply_date', models.DateField(blank=True, null=True)),
                ('farmerName', models.CharField(blank=True, max_length=100, null=True)),
                ('applied_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applied_machines', to='ceapp.farmerprofile')),
                ('machinery', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ceapp.machinery')),
            ],
        ),
    ]
