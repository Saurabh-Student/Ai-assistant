import os
import sys
from dotenv import load_dotenv

print("Starting debug script...")
print("Python version:", sys.version)
print("Current working directory:", os.getcwd())

# Load your API keys from .env
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_SEARCH_API_KEY")
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")

print("\nEnvironment variables:")
print(f"GOOGLE_API_KEY: {'Set' if GOOGLE_API_KEY else 'Not set'}")
print(f"SEARCH_ENGINE_ID: {'Set' if SEARCH_ENGINE_ID else 'Not set'}")

print("\nTesting DuckDuckGo search...")
try:
    from duckduckgo_search import DDGS
    print("DuckDuckGo imported successfully")
    
    ddgs = DDGS()
    print("DDGS instance created")
    
    results = ddgs.text("Python programming", max_results=3)
    print("Search executed")
    print("Results type:", type(results))
    
    results_list = list(results)
    print("Results list length:", len(results_list))
    
    for i, result in enumerate(results_list):
        print(f"Result {i+1}:")
        print(f"  Title: {result.get('title', 'No title')}")
        print(f"  Link: {result.get('href', 'No link')}")
        if i >= 2:  # Only show first 3 results
            break
    print("DuckDuckGo search completed successfully")
except Exception as e:
    print(f"DuckDuckGo search failed: {e}")
    import traceback
    traceback.print_exc()

print("\nDebug script completed")
