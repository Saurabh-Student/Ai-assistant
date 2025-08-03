import os
from googleapiclient.discovery import build

# Use the API key from the documentation
GOOGLE_API_KEY = 'AIzaSyB0b36lqutN3K7DHuPAuBPOnAhFYpfn8RU'
SEARCH_ENGINE_ID = 'f469efe96a9aa4e2f'

print("Testing Google Custom Search API directly...")

try:
    print("Building service...")
    service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)
    print("Service built successfully!")
    
    print("Executing search...")
    results = service.cse().list(q="test", cx=SEARCH_ENGINE_ID, num=1).execute()
    print("Search executed successfully!")
    print("Results keys:", results.keys())
    if 'items' in results:
        print("Number of items:", len(results['items']))
        print("First item title:", results['items'][0].get('title', 'No title'))
    else:
        print("No items found in results")
except Exception as e:
    print("Error:", str(e))
    import traceback
    traceback.print_exc()
