import os
import sys
from dotenv import load_dotenv
from jarvis_search import google_search

# Load environment variables
load_dotenv()

if __name__ == "__main__":
    # Test the google_search function directly
    print("Testing Google Search function...")
    try:
        result = google_search("Python programming")
        print("Search successful!")
        print("Result:")
        print(result)
    except Exception as e:
        print(f"Search failed: {e}")
        import traceback
        traceback.print_exc()
