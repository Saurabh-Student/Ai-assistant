import os
from dotenv import load_dotenv

# Load your API keys from .env
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_SEARCH_API_KEY")
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")

print("Environment variables:")
print(f"GOOGLE_API_KEY: {'Set' if GOOGLE_API_KEY else 'Not set'}")
print(f"SEARCH_ENGINE_ID: {'Set' if SEARCH_ENGINE_ID else 'Not set'}")

# Test DuckDuckGo search directly
try:
    from duckduckgo_search import DDGS
    ddgs = DDGS()
    results = ddgs.text("Python programming", max_results=3)
    print("\nDuckDuckGo search results:")
    for result in results:
        print(f"Title: {result.get('title', 'No title')}")
        print(f"Link: {result.get('href', 'No link')}")
        print("---")
except Exception as e:
    print(f"\nDuckDuckGo search failed: {e}")
