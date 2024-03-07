# Generated by Django 4.2.4 on 2024-03-07 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0191_remove_applicationmachinery_applied_by_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddMachinery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machinery_photo', models.ImageField(upload_to='machinery_photos/')),
                ('mname', models.CharField(max_length=255)),
                ('count', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('days', models.IntegerField()),
            ],
        ),
    ]
