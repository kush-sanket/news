import requests
import json

try:
    print("Testing API response format...")
    response = requests.get('http://127.0.0.1:8000/api/news/')
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print(f"Response Type: {type(data)}")
        
        if isinstance(data, list):
            print("✅ SUCCESS: API returns simple array format!")
            print(f"Number of articles: {len(data)}")
            if len(data) > 0:
                print("\nFirst article structure:")
                first_article = data[0]
                for key, value in first_article.items():
                    if key == 'description':
                        print(f"  {key}: {str(value)[:100]}...")
                    else:
                        print(f"  {key}: {value}")
                
                print(f"\nSample JSON format (first 2 articles):")
                print(json.dumps(data[:2], indent=2))
        else:
            print("❌ FAILED: API still returns paginated format")
            print(f"Response structure: {list(data.keys()) if isinstance(data, dict) else 'Unknown'}")
    else:
        print(f"Error: {response.status_code} - {response.text}")
        
except requests.exceptions.ConnectionError:
    print("❌ ERROR: Could not connect to Django server.")
    print("Make sure Django server is running on http://127.0.0.1:8000")
except Exception as e:
    print(f"❌ ERROR: {e}")