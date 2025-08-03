import os
from dotenv import load_dotenv
from jarvis_search import google_search

def main():
    # Load environment variables
    load_dotenv()
    
    # Test the improved google_search function
    print("Testing Improved Google Search function...")
    try:
        result = google_search("Python programming")
        print("✅ Search function working correctly!")
        print("Sample result:")
        print(result[:300] + "..." if len(result) > 300 else result)
    except Exception as e:
        print(f"❌ Search function failed: {e}")
        return False
    
    # Test with a different query
    print("\nTesting with another query...")
    try:
        result = google_search("current weather in New York")
        print("✅ Second search working correctly!")
        print("Sample result:")
        print(result[:300] + "..." if len(result) > 300 else result)
    except Exception as e:
        print(f"❌ Second search failed: {e}")
        return False
    
    return True

if __name__ == "__main__":
    main()
