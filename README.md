# News API Django Backend

A Django REST API for managing news articles, designed to be consumed by React Native applications.

## Features

- RESTful API endpoints for news articles
- CORS enabled for React Native/mobile app integration
- PostgreSQL/SQLite database support
- Admin interface for content management
- Pagination support
- Category-based news filtering

## API Endpoints

### Base URL: `http://127.0.0.1:8000`

### 1. Get All News Articles
**GET** `/api/news/`

Returns a paginated list of all news articles.

**Response:**
```json
{
  "count": 5,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": "1",
      "title": "Breaking: Major Tech Company Announces Revolutionary AI Breakthrough",
      "description": "A leading technology company has unveiled...",
      "urlToImage": "https://share.google/images/47AC9Zl1LQnPyGgLF",
      "publishedAt": "2024-01-15T10:00:00Z",
      "source": {
        "name": "Tech Today"
      },
      "category": "technology",
      "url": "https://example.com/tech-news-1"
    }
  ]
}
```

### 2. Get Specific News Article
**GET** `/api/news/{id}/`

Returns a specific news article by ID.

**Response:**
```json
{
  "id": "1",
  "title": "Breaking: Major Tech Company Announces Revolutionary AI Breakthrough",
  "description": "A leading technology company has unveiled...",
  "urlToImage": "https://share.google/images/47AC9Zl1LQnPyGgLF",
  "publishedAt": "2024-01-15T10:00:00Z",
  "source": {
    "name": "Tech Today"
  },
  "category": "technology",
  "url": "https://example.com/tech-news-1"
}
```

### 3. Create New News Article
**POST** `/api/news/`

Creates a new news article.

**Request Body:**
```json
{
  "id": "unique-id",
  "title": "Your News Title",
  "description": "Detailed description of the news article...",
  "urlToImage": "https://example.com/image.jpg",
  "publishedAt": "2024-01-15T10:00:00Z",
  "source": {
    "name": "Source Name"
  },
  "category": "technology",
  "url": "https://example.com/article-url"
}
```

**Response:** Returns the created article with status code 201.

### 4. Update News Article
**PUT/PATCH** `/api/news/{id}/`

Updates an existing news article.

### 5. Delete News Article
**DELETE** `/api/news/{id}/`

Deletes a news article.

## Available Categories

- `technology`
- `general`
- `business` 
- `sports`
- `health`
- `entertainment`
- `science`

## React Native Integration

### Installation
Install axios or fetch for HTTP requests:
```bash
npm install axios
```

### Example React Native Service

```javascript
// newsService.js
import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000/api'; // Change to your server IP for device testing

class NewsService {
  
  // Get all news articles
  static async getAllNews(page = 1) {
    try {
      const response = await axios.get(`${API_BASE_URL}/news/?page=${page}`);
      return response.data;
    } catch (error) {
      console.error('Error fetching news:', error);
      throw error;
    }
  }

  // Get specific news article
  static async getNewsById(id) {
    try {
      const response = await axios.get(`${API_BASE_URL}/news/${id}/`);
      return response.data;
    } catch (error) {
      console.error('Error fetching news by ID:', error);
      throw error;
    }
  }

  // Create new news article
  static async createNews(newsData) {
    try {
      const response = await axios.post(`${API_BASE_URL}/news/`, newsData, {
        headers: {
          'Content-Type': 'application/json',
        },
      });
      return response.data;
    } catch (error) {
      console.error('Error creating news:', error);
      throw error;
    }
  }

  // Filter news by category
  static async getNewsByCategory(category, page = 1) {
    try {
      const response = await axios.get(`${API_BASE_URL}/news/?category=${category}&page=${page}`);
      return response.data;
    } catch (error) {
      console.error('Error fetching news by category:', error);
      throw error;
    }
  }
}

export default NewsService;
```

### Example React Native Component

```javascript
// NewsScreen.js
import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  FlatList,
  TouchableOpacity,
  Image,
  StyleSheet,
  RefreshControl,
} from 'react-native';
import NewsService from './newsService';

const NewsScreen = () => {
  const [news, setNews] = useState([]);
  const [loading, setLoading] = useState(false);
  const [refreshing, setRefreshing] = useState(false);

  useEffect(() => {
    fetchNews();
  }, []);

  const fetchNews = async () => {
    try {
      setLoading(true);
      const response = await NewsService.getAllNews();
      setNews(response.results || response);
    } catch (error) {
      console.error('Failed to fetch news:', error);
    } finally {
      setLoading(false);
    }
  };

  const onRefresh = async () => {
    setRefreshing(true);
    await fetchNews();
    setRefreshing(false);
  };

  const renderNewsItem = ({ item }) => (
    <TouchableOpacity style={styles.newsItem}>
      {item.urlToImage && (
        <Image source={{ uri: item.urlToImage }} style={styles.newsImage} />
      )}
      <View style={styles.newsContent}>
        <Text style={styles.newsTitle}>{item.title}</Text>
        <Text style={styles.newsDescription} numberOfLines={3}>
          {item.description}
        </Text>
        <View style={styles.newsFooter}>
          <Text style={styles.newsSource}>{item.source.name}</Text>
          <Text style={styles.newsCategory}>{item.category}</Text>
        </View>
      </View>
    </TouchableOpacity>
  );

  return (
    <View style={styles.container}>
      <FlatList
        data={news}
        renderItem={renderNewsItem}
        keyExtractor={(item) => item.id}
        refreshControl={
          <RefreshControl refreshing={refreshing} onRefresh={onRefresh} />
        }
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
  },
  newsItem: {
    backgroundColor: 'white',
    margin: 10,
    borderRadius: 8,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 3,
  },
  newsImage: {
    width: '100%',
    height: 200,
    borderTopLeftRadius: 8,
    borderTopRightRadius: 8,
  },
  newsContent: {
    padding: 15,
  },
  newsTitle: {
    fontSize: 16,
    fontWeight: 'bold',
    marginBottom: 8,
  },
  newsDescription: {
    fontSize: 14,
    color: '#666',
    marginBottom: 10,
  },
  newsFooter: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  newsSource: {
    fontSize: 12,
    color: '#888',
  },
  newsCategory: {
    fontSize: 12,
    color: '#007AFF',
    fontWeight: '500',
  },
});

export default NewsScreen;
```

## Setup Instructions

### 1. Install Dependencies
```bash
pip install django djangorestframework django-cors-headers
```

### 2. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Load Sample Data
```bash
python manage.py load_sample_data
```

### 4. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 5. Start Development Server
```bash
python manage.py runserver
```

### 6. Access Admin Interface
Visit `http://127.0.0.1:8000/admin/` to manage news articles through the web interface.

## Testing the API

### Using curl:
```bash
# Get all news
curl -X GET http://127.0.0.1:8000/api/news/

# Get specific news
curl -X GET http://127.0.0.1:8000/api/news/1/

# Create new news
curl -X POST http://127.0.0.1:8000/api/news/ \
  -H "Content-Type: application/json" \
  -d '{
    "id": "test-123",
    "title": "Test Article",
    "description": "This is a test article",
    "urlToImage": "https://example.com/image.jpg",
    "publishedAt": "2024-01-15T10:00:00Z",
    "source": {"name": "Test Source"},
    "category": "technology",
    "url": "https://example.com/test"
  }'
```

### Using the provided test script:
```bash
python test_api.py
```

## Important Notes for React Native

1. **Change Server IP**: When testing on a physical device, replace `127.0.0.1` with your computer's IP address.

2. **CORS Configuration**: The app is configured to allow all origins during development. For production, update `CORS_ALLOWED_ORIGINS` in settings.py.

3. **Error Handling**: Always implement proper error handling in your React Native app to handle network failures and API errors.

4. **Data Validation**: The API validates required fields. Make sure your React Native app sends all required fields when creating/updating articles.

5. **Pagination**: The API returns paginated results. Use the `next` and `previous` fields in the response to implement pagination in your React Native app.

## Production Considerations

- Use a production database (PostgreSQL)
- Set up proper authentication/authorization
- Configure HTTPS
- Set DEBUG=False in settings
- Use environment variables for sensitive settings
- Deploy using a production WSGI server (gunicorn, uwsgi)

The API is now ready to be consumed by your React Native application!