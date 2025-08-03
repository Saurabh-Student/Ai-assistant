import os
from dotenv import load_dotenv
from jarvis_search import google_search

# Load environment variables
load_dotenv()

if __name__ == "__main__":
    # Test the google_search function
    query = "Python programming"
    print(f"Searching for: {query}")
    result = google_search(query)
    print("Search results:")
    print(result)
