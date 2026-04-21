from django.urls import path
from . import views

app_name = 'news_api'

urlpatterns = [
    # Class-based views
    path('api/news/', views.NewsArticleListCreateView.as_view(), name='news-list-create'),
    path('api/news/<str:id>/', views.NewsArticleDetailView.as_view(), name='news-detail'),
    
    # Function-based view (alternative)
    path('api/articles/', views.news_articles_api, name='articles-api'),
]