# Generated by Django 4.0.2 on 2022-02-04 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0009_rename_friends_profile_follower'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['id']},
        ),
    ]