import requests

# Use the API key from the documentation
GOOGLE_API_KEY = 'AIzaSyB0b36lqutN3K7DHuPAuBPOnAhFYpfn8RU'
SEARCH_ENGINE_ID = 'f469efe96a9aa4e2f'

print("Testing Google Custom Search API with requests...")

try:
    url = f"https://www.googleapis.com/customsearch/v1"
    params = {
        'key': GOOGLE_API_KEY,
        'cx': SEARCH_ENGINE_ID,
        'q': 'test',
        'num': 1
    }
    
    print("Making request to Google Custom Search API...")
    response = requests.get(url, params=params, timeout=10)
    
    print(f"Response status code: {response.status_code}")
    print(f"Response headers: {dict(response.headers)}")
    
    if response.status_code == 200:
        print("✅ Request successful!")
        results = response.json()
        print("Results keys:", results.keys())
        if 'items' in results:
            print("Number of items:", len(results['items']))
            print("First item title:", results['items'][0].get('title', 'No title'))
        else:
            print("No items found in results")
            print("Full response:", results)
    else:
        print(f"❌ Request failed with status code: {response.status_code}")
        print("Response text:", response.text)
        
except Exception as e:
    print("Error:", str(e))
    import traceback
    traceback.print_exc()
