import os
from dotenv import load_dotenv
from jarvis_search import enhanced_google_search, google_search_fallback, google_search

def main():
    # Load environment variables
    load_dotenv()
    
    print("Testing Google Search Functionality")
    print("=" * 40)
    
    # Check if Google API credentials are available
    GOOGLE_API_KEY = os.getenv("GOOGLE_SEARCH_API_KEY")
    SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")
    
    print(f"Google API Key available: {'Yes' if GOOGLE_API_KEY else 'No'}")
    print(f"Search Engine ID available: {'Yes' if SEARCH_ENGINE_ID else 'No'}")
    
    if not GOOGLE_API_KEY or not SEARCH_ENGINE_ID:
        print("\n⚠️  Google API credentials not found in environment variables.")
        print("Please set GOOGLE_SEARCH_API_KEY and SEARCH_ENGINE_ID in your .env file.")
        print("The search will fall back to DuckDuckGo in this case.")
        return
    
    # Test enhanced Google search
    print("\n1. Testing Enhanced Google Search:")
    try:
        result = enhanced_google_search("latest technology news")
        print("✅ Enhanced Google Search successful!")
        print("Sample result:")
        print(result[:300] + ("..." if len(result) > 300 else ""))
    except Exception as e:
        print(f"❌ Enhanced Google Search failed: {e}")
    
    # Test Google search fallback
    print("\n2. Testing Google Search Fallback:")
    try:
        result = google_search_fallback("current weather")
        print("✅ Google Search Fallback successful!")
        print("Sample result:")
        print(result[:300] + ("..." if len(result) > 300 else ""))
    except Exception as e:
        print(f"❌ Google Search Fallback failed: {e}")
    
    # Test main Google search function
    print("\n3. Testing Main Google Search Function:")
    try:
        result = google_search("breaking news today")
        print("✅ Main Google Search successful!")
        print("Sample result:")
        print(result[:300] + ("..." if len(result) > 300 else ""))
    except Exception as e:
        print(f"❌ Main Google Search failed: {e}")

if __name__ == "__main__":
    main()
