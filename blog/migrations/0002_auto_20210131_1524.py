# Generated by Django 2.2 on 2021-01-31 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='detail_image',
        ),
        migrations.AddField(
            model_name='post',
            name='list_image',
            field=models.ImageField(blank=True, null=True, upload_to='blog/'),
        ),
    ]
