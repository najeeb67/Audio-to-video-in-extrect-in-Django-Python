from rest_framework import serializers
from .models import *

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id','video_file','uploaded_at')
