# Generated by Django 2.2 on 2021-02-02 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210202_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.CharField(default='Barcelona', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='phone',
            field=models.CharField(default='54546648456', max_length=100),
            preserve_default=False,
        ),
    ]