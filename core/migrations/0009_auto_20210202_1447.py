# Generated by Django 2.2 on 2021-02-02 13:47

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0008_auto_20210202_1331'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='Customer',
        ),
    ]
