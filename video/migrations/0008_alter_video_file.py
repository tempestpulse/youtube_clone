# Generated by Django 5.0 on 2023-12-29 16:49

import video.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0007_video_dislikes_remove_video_likes_video_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='file',
            field=models.FileField(upload_to='media/videos/', validators=[video.validators.validate_file_extension]),
        ),
    ]
