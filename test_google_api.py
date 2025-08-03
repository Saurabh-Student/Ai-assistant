import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

# Load your API keys from .env
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_SEARCH_API_KEY")
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")

print("GOOGLE_SEARCH_API_KEY:", GOOGLE_API_KEY)
print("SEARCH_ENGINE_ID:", SEARCH_ENGINE_ID)

if not GOOGLE_API_KEY or not SEARCH_ENGINE_ID:
    print("Error: API keys not found!")
    exit(1)

try:
    print("Building service...")
    service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)
    print("Service built successfully!")
    
    print("Executing search...")
    results = service.cse().list(q="test", cx=SEARCH_ENGINE_ID, num=1).execute()
    print("Search executed successfully!")
    print("Results:", results)
except Exception as e:
    print("Error:", str(e))
    import traceback
    traceback.print_exc()
