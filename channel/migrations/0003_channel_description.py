# Generated by Django 5.0 on 2023-12-25 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0002_alter_channel_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='description',
            field=models.TextField(blank=True, max_length=5000),
        ),
    ]
