# Generated by Django 5.0 on 2023-12-30 15:37

import video.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0008_alter_video_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='file',
            field=models.FileField(upload_to='videos/', validators=[video.validators.validate_file_extension]),
        ),
        migrations.AlterField(
            model_name='video',
            name='thumbnail',
            field=models.ImageField(blank=True, default='thumbnails/default_thumbnail.jpg', null=True, upload_to='thumbnails/'),
        ),
    ]
