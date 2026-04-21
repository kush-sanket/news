from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import NewsArticle
from .serializers import NewsArticleSerializer
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class NewsArticleListCreateView(generics.ListCreateAPIView):
    """
    GET: Retrieve all news articles as simple array
    POST: Create a new news article
    """
    queryset = NewsArticle.objects.all()
    serializer_class = NewsArticleSerializer
    pagination_class = None  # Disable pagination to return simple array

    def list(self, request, *args, **kwargs):
        """Override list method to return simple array format"""
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class NewsArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve a specific news article
    PUT/PATCH: Update a news article
    DELETE: Delete a news article
    """
    queryset = NewsArticle.objects.all()
    serializer_class = NewsArticleSerializer
    lookup_field = 'id'


@csrf_exempt
@api_view(['GET', 'POST'])
def news_articles_api(request):
    """
    Simple function-based view for news articles
    GET: Return all news articles
    POST: Create a new news article
    """
    if request.method == 'GET':
        articles = NewsArticle.objects.all()
        serializer = NewsArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return Response({'error': 'Invalid JSON'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = NewsArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
