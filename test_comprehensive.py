import os
import sys
from dotenv import load_dotenv
from jarvis_search import google_search

# Add the current directory to Python path
sys.path.insert(0, '.')

# Load environment variables
load_dotenv()

def test_google_search():
    """Test the google_search function directly"""
    print("Testing Google Search function...")
    try:
        result = google_search("Python programming")
        print("Search successful!")
        print("Result:")
        print(result)
        return True
    except Exception as e:
        print(f"Search failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_api_keys():
    """Test if API keys are loaded correctly"""
    print("Testing API keys...")
    google_api_key = os.getenv("GOOGLE_SEARCH_API_KEY")
    search_engine_id = os.getenv("SEARCH_ENGINE_ID")
    
    if not google_api_key:
        print("ERROR: GOOGLE_SEARCH_API_KEY not found in environment variables")
        return False
    
    if not search_engine_id:
        print("ERROR: SEARCH_ENGINE_ID not found in environment variables")
        return False
    
    print("API keys loaded successfully!")
    return True

if __name__ == "__main__":
    print("Running comprehensive test...")
    
    # Test API keys first
    if not test_api_keys():
        print("API key test failed. Exiting.")
        sys.exit(1)
    
    # Test Google Search function
    if not test_google_search():
        print("Google Search test failed. Exiting.")
        sys.exit(1)
    
    print("All tests passed!")
