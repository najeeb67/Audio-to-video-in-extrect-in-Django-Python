from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Video
from .serializers import VideoSerializer
from moviepy.editor import VideoFileClip
import os


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        video = Video.objects.get(pk=serializer.data['id'])
        self.extract_audio(video)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def extract_audio(self, video):
        video_path = video.video_file.path
        audio_path = os.path.splitext(video_path)[0] + '.mp3'
        
        with VideoFileClip(video_path) as video_clip:
            audio_clip = video_clip.audio
            audio_clip.write_audiofile(audio_path)
            
        video.audio_file.name = audio_path.split('/')[-1]
        video.save()



