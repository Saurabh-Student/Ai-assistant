import traceback
from jarvis_search import google_search

# Test the google_search function
try:
    print("Testing google_search function...")
    result = google_search("test query")
    print("SUCCESS: google_search function executed")
    print("Result:", result)
except Exception as e:
    print("ERROR:", str(e))
    print("Traceback:")
    traceback.print_exc()
