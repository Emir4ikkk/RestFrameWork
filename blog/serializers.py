from rest_framework import serializers
from .models import Publication

class PublicationSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Publication
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at']
