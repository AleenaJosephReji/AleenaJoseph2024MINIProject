# Generated by Django 4.2.4 on 2023-09-25 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ceapp', '0046_alter_crop_crop_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='ward',
            new_name='wardname',
        ),
    ]