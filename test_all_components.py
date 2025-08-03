import os
import sys
from dotenv import load_dotenv

# Add the current directory to Python path
sys.path.insert(0, '.')

# Load environment variables
load_dotenv()

def test_env_vars():
    """Test if environment variables are loaded correctly"""
    print("Testing environment variables...")
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

def test_imports():
    """Test if all required modules can be imported"""
    print("Testing imports...")
    try:
        from googleapiclient.discovery import build
        print("googleapiclient: OK")
        
        from jarvis_search import google_search
        print("jarvis_search: OK")
        
        return True
    except ImportError as e:
        print(f"Import failed: {e}")
        return False

def test_google_search():
    """Test the google_search function directly"""
    print("Testing Google Search function...")
    try:
        from jarvis_search import google_search
        result = google_search("Python programming")
        print("Search successful!")
        print("Result preview:")
        print(result[:200] + "..." if len(result) > 200 else result)
        return True
    except Exception as e:
        print(f"Search failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Running comprehensive test of all components...")
    
    # Test environment variables
    if not test_env_vars():
        print("Environment variables test failed. Exiting.")
        sys.exit(1)
    
    # Test imports
    if not test_imports():
        print("Import test failed. Exiting.")
        sys.exit(1)
    
    # Test Google Search function
    if not test_google_search():
        print("Google Search test failed. Exiting.")
        sys.exit(1)
    
    print("\nAll tests passed! The Google Search integration is working correctly.")
