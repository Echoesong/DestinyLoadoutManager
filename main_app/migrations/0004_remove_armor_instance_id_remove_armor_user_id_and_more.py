# Generated by Django 4.2 on 2023-04-20 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_weapon_armor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='armor',
            name='instance_id',
        ),
        migrations.RemoveField(
            model_name='armor',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='weapon',
            name='instance_id',
        ),
        migrations.RemoveField(
            model_name='weapon',
            name='user_id',
        ),
    ]
