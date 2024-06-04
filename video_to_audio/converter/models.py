from django.db import models

# Create your models here.

class Video(models.Model):
    video_file = models.FileField(upload_to='videos/' , blank=True, null=True)
    audio_file = models.FileField(upload_to='audios/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
