# Generated by Django 2.2 on 2021-02-02 18:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
