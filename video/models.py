from channel.models import User, Channel
from django.db import models
from .validators import validate_file_extension


class Tag(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Video(models.Model):
    DEFAULT_THUMBNAIL = 'thumbnails/default_thumbnail.jpg'

    title = models.CharField(max_length=80)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, null=True, on_delete=models.CASCADE)
    file = models.FileField(upload_to='videos/', validators=[validate_file_extension])
    thumbnail = models.ImageField(default=DEFAULT_THUMBNAIL, upload_to='thumbnails/', blank=True, null=True)
    description = models.TextField(max_length=5000, blank=True, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag, blank=True)
    likes = models.ManyToManyField(User, related_name='video_like')
    dislikes = models.ManyToManyField(User, related_name='video_dislike')
    views = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.thumbnail:
            self.thumbnail = self.DEFAULT_THUMBNAIL
        super(Video, self).save(*args, **kwargs)

    @property
    def dislike_count(self):
        return self.dislikes.count()

    def dislike_status(self, user):
        return self.dislikes.filter(pk=user.id).exists()

    @property
    def like_count(self):
        return self.likes.count()

    def like_status(self, user):
        return self.likes.filter(pk=user.id).exists()

    @property
    def comment_count(self):
        return self.comments.count()

    def __str__(self):
        return self.title


class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=10000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} -- {self.video}"


class WatchLater(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} -- {self.video}"
