from django.contrib import admin
from .models import NewsArticle


@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'source_name', 'published_at', 'created_at']
    list_filter = ['category', 'source_name', 'published_at', 'created_at']
    search_fields = ['title', 'description', 'id', 'source_name']
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'published_at'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('id', 'title', 'description', 'category')
        }),
        ('Links', {
            'fields': ('url', 'url_to_image')
        }),
        ('Source & Publishing', {
            'fields': ('source_name', 'published_at')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
