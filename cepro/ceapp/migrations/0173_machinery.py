# Generated by Django 4.2.4 on 2024-03-06 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0172_total_paid_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Machinery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mname', models.CharField(max_length=100)),
                ('count', models.CharField(max_length=100)),
                ('price', models.IntegerField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
