# Generated by Django 5.1.1 on 2024-09-24 16:43

import django.contrib.auth.models
import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_human_managers_alter_human_phone'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='human',
            managers=[
                ('activated', django.db.models.manager.Manager()),
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
