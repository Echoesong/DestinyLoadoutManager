# Generated by Django 4.2 on 2023-04-21 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_profile_destiny2_membership_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Armor',
        ),
        migrations.DeleteModel(
            name='Weapon',
        ),
    ]
