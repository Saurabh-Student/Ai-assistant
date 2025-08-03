import os
import sys
from dotenv import load_dotenv
from jarvis_search import google_search, enhanced_duckduckgo_search

def test_search_functionality():
    """Test the search functionality comprehensively"""
    print("Testing Jarvis Search Functionality")
    print("=" * 50)
    
    # Test DuckDuckGo search directly
    print("\n1. Testing DuckDuckGo search directly:")
    try:
        result = enhanced_duckduckgo_search("current weather in New York")
        print("✅ DuckDuckGo search successful!")
        print("Sample result (first 200 chars):")
        print(result[:200] + ("..." if len(result) > 200 else ""))
    except Exception as e:
        print(f"❌ DuckDuckGo search failed: {e}")
        import traceback
        traceback.print_exc()
    
    # Test main search function
    print("\n2. Testing main search function:")
    try:
        result = google_search("latest technology news")
        print("✅ Main search function successful!")
        print("Sample result (first 300 chars):")
        print(result[:300] + ("..." if len(result) > 300 else ""))
    except Exception as e:
        print(f"❌ Main search function failed: {e}")
        import traceback
        traceback.print_exc()
    
    # Test with different queries
    print("\n3. Testing with various queries:")
    queries = [
        "current time in Tokyo",
        "latest sports scores",
        "weather forecast for tomorrow"
    ]
    
    for i, query in enumerate(queries, 1):
        print(f"   Test {i}: '{query}'")
        try:
            result = google_search(query)
            status = "✅ Success" if "sorry" not in result.lower() and "error" not in result.lower() else "⚠️  No results"
            print(f"   Status: {status}")
        except Exception as e:
            print(f"   Status: ❌ Failed - {e}")
    
    print("\n" + "=" * 50)
    print("Comprehensive testing completed!")

if __name__ == "__main__":
    # Load environment variables
    load_dotenv()
    
    # Add current directory to Python path
    sys.path.insert(0, os.getcwd())
    
    test_search_functionality()
