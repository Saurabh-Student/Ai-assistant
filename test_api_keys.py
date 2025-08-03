import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

# Load environment variables
load_dotenv()

# Get API keys
GOOGLE_API_KEY = os.getenv("GOOGLE_SEARCH_API_KEY")
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")

print("API Keys:")
print(f"GOOGLE_SEARCH_API_KEY: {GOOGLE_API_KEY}")
print(f"SEARCH_ENGINE_ID: {SEARCH_ENGINE_ID}")

# Test if we can build the service
try:
    service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)
    print("Service built successfully!")
    
    # Test a simple search
    try:
        results = service.cse().list(q="test", cx=SEARCH_ENGINE_ID, num=1).execute()
        print("Search executed successfully!")
        print(f"Found {len(results.get('items', []))} results")
    except Exception as e:
        print(f"Search failed: {e}")
except Exception as e:
    print(f"Service build failed: {e}")
