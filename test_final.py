import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

# Load environment variables
load_dotenv()

# Get API keys
GOOGLE_API_KEY = os.getenv("GOOGLE_SEARCH_API_KEY")
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")

print("Testing Google Custom Search API...")
print(f"GOOGLE_API_KEY: {GOOGLE_API_KEY[:10]}...{GOOGLE_API_KEY[-5:] if GOOGLE_API_KEY else 'None'}")
print(f"SEARCH_ENGINE_ID: {SEARCH_ENGINE_ID}")

if not GOOGLE_API_KEY or not SEARCH_ENGINE_ID:
    print("ERROR: Missing API keys in environment variables")
    exit(1)

try:
    # Build the service
    service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)
    print("Service built successfully!")
    
    # Test a simple search
    print("Executing test search...")
    results = service.cse().list(q="Python programming", cx=SEARCH_ENGINE_ID, num=3).execute()
    
    print("Search executed successfully!")
    print(f"Found {len(results.get('items', []))} results")
    
    if 'items' in results:
        for i, item in enumerate(results['items'][:3], 1):
            print(f"\nResult {i}:")
            print(f"Title: {item.get('title', 'N/A')}")
            print(f"Link: {item.get('link', 'N/A')}")
            print(f"Snippet: {item.get('snippet', 'N/A')[:100]}...")
    else:
        print("No items found in search results")
        
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()
