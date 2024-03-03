from rest_framework import serializers
from .models import YoutubeVideo

class YouTubeVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoutubeVideo
        fields = ['title', 'channel']
    
