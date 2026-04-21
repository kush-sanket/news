#!/usr/bin/env python
"""
Test script for the News API endpoints
Run this to test both GET and POST endpoints
"""
import requests
import json
from datetime import datetime

# API endpoints
BASE_URL = "http://127.0.0.1:8000"
NEWS_API_URL = f"{BASE_URL}/api/news/"
ARTICLES_API_URL = f"{BASE_URL}/api/articles/"

def test_get_news():
    """Test GET endpoint to retrieve all news"""
    print("Testing GET /api/news/")
    try:
        response = requests.get(NEWS_API_URL)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Found {len(data.get('results', data))} articles")
            if data:
                # Print first article as example
                first_article = data.get('results', data)[0] if 'results' in data else data[0]
                print(f"First article: {first_article.get('title', 'No title')[:50]}...")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Error: {e}")
    print("-" * 50)

def test_post_news():
    """Test POST endpoint to create a new news article"""
    print("Testing POST /api/news/")
    
    new_article = {
        "id": "test-001",
        "title": "Test Article: Django API Working Perfectly",
        "description": "This is a test article created via the POST API endpoint to verify that the Django news API is working correctly. The article demonstrates the ability to create new news items programmatically.",
        "urlToImage": "https://example.com/test-image.jpg",
        "publishedAt": datetime.now().isoformat() + "Z",
        "source": {"name": "Test Source"},
        "category": "technology",
        "url": "https://example.com/test-article"
    }
    
    try:
        response = requests.post(
            NEWS_API_URL,
            headers={'Content-Type': 'application/json'},
            data=json.dumps(new_article)
        )
        print(f"Status Code: {response.status_code}")
        if response.status_code == 201:
            data = response.json()
            print(f"Created article: {data.get('title', 'No title')}")
            print(f"Article ID: {data.get('id', 'No ID')}")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Error: {e}")
    print("-" * 50)

def test_get_specific_article():
    """Test GET endpoint for a specific article"""
    print("Testing GET /api/news/<id>/")
    article_id = "1"  # Test with the first sample article
    
    try:
        response = requests.get(f"{NEWS_API_URL}{article_id}/")
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Article: {data.get('title', 'No title')[:50]}...")
            print(f"Category: {data.get('category', 'No category')}")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Error: {e}")
    print("-" * 50)

if __name__ == "__main__":
    print("=== News API Test Script ===")
    print("Make sure Django server is running on http://127.0.0.1:8000")
    print("=" * 50)
    
    test_get_news()
    test_get_specific_article()
    test_post_news()
    
    print("=== Test Complete ===")