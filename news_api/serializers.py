from rest_framework import serializers
from .models import NewsArticle


class NewsArticleSerializer(serializers.ModelSerializer):
    """
    Simple serializer for single NewsArticle table
    Maps database fields to API JSON format
    """
    # Map database field names to your desired JSON field names
    urlToImage = serializers.URLField(source='url_to_image', required=False, allow_null=True)
    publishedAt = serializers.DateTimeField(source='published_at')
    source = serializers.SerializerMethodField()  # Custom field for nested source object
    
    class Meta:
        model = NewsArticle
        fields = ['id', 'title', 'description', 'urlToImage', 'publishedAt', 'source', 'category', 'url']
    
    def get_source(self, obj):
        """Convert source_name field to nested object format"""
        return {"name": obj.source_name}
    
    def create(self, validated_data):
        """Handle creation with source nested object"""
        source_data = validated_data.pop('source', {})
        if source_data:
            validated_data['source_name'] = source_data['name']
        return NewsArticle.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """Handle updates with source nested object"""
        source_data = validated_data.pop('source', None)
        if source_data:
            instance.source_name = source_data['name']
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance