import os
import sys

# Set environment variables directly
os.environ['GOOGLE_SEARCH_API_KEY'] = 'AIzaSyB0b36lqutN3K7DHuPAuBPOnAhFYpfn8RU'
os.environ['SEARCH_ENGINE_ID'] = 'f469efe96a9aa4e2f'

print("Environment variables:")
print(f"GOOGLE_SEARCH_API_KEY: {os.getenv('GOOGLE_SEARCH_API_KEY')}")
print(f"SEARCH_ENGINE_ID: {os.getenv('SEARCH_ENGINE_ID')}")

print("\nTesting imports:")
try:
    from jarvis_search import google_search
    print("✓ jarvis_search imported successfully")
except Exception as e:
    print(f"✗ Failed to import jarvis_search: {e}")
    import traceback
    traceback.print_exc()

print("\nTesting search function:")
try:
    result = google_search("test")
    print("✓ Search function executed successfully")
    print(f"Result preview: {result[:100]}...")
except Exception as e:
    print(f"✗ Search function failed: {e}")
    import traceback
    traceback.print_exc()
