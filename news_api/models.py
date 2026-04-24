from django.db import models
from django.utils import timezone


class NewsArticle(models.Model):
    """Single table for news articles - simplified model"""
    CATEGORY_CHOICES = [
        ('technology', 'Technology'),
        ('general', 'General'),
        ('business', 'Business'),
        ('sports', 'Sports'),
        ('health', 'Health'),
        ('entertainment', 'Entertainment'),
        ('science', 'Science'),
    ]
    
    id = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=500)
    description = models.TextField()
    url_to_image = models.URLField(max_length=500, null=True, blank=True)
    published_at = models.DateTimeField(default=timezone.now)
    source_name = models.CharField(max_length=200, default='Unknown Source')  # Simple CharField with default
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    url = models.URLField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-published_at']
    
    def __str__(self):
        return self.title
