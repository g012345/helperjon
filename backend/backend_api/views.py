from django.shortcuts import render
from rest_framework.views import APIView
from .models import YoutubeVideo
from .serializer import YouTubeVideoSerializer
from rest_framework.response import Response

class YouTubeVideoView(APIView):
    def get(self, request):
        output = [
            {
                "title": output.title,
                "channel": output.channel
            } for output in YoutubeVideo.objects.all()
        
        ]
        return Response(output)
    
    def post(self, request):
        serializer = YouTubeVideoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)



