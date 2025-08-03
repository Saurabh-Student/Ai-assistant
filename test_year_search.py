import os
from dotenv import load_dotenv
from jarvis_search import google_search, is_year_search

def main():
    # Load environment variables
    load_dotenv()
    
    print("Testing Year-Specific Search Functionality")
    print("=" * 50)
    
    # Test the year detection function
    print("\n1. Testing year detection function:")
    test_queries = [
        "2025 technology trends",
        "events in 2025",
        "what will happen in 2025",
        "2025",
        "current weather",
        "latest news",
        "2023 Olympics",
        "future of AI in 2030"
    ]
    
    for query in test_queries:
        is_year = is_year_search(query)
        print(f"   '{query}' -> Year search: {is_year}")
    
    # Test actual searches for years
    print("\n2. Testing searches for specific years:")
    year_queries = [
        "2025 technology predictions",
        "2030 future trends",
        "2024 election results"
    ]
    
    for query in year_queries:
        print(f"\n   Searching for: '{query}'")
        try:
            result = google_search(query)
            print("   ✅ Search completed!")
            # Show first 200 characters of result
            print("   Sample result:", result[:200] + ("..." if len(result) > 200 else ""))
        except Exception as e:
            print(f"   ❌ Search failed: {e}")
    
    # Test current searches still work
    print("\n3. Testing current searches still work:")
    current_queries = [
        "current weather",
        "latest news",
        "today's sports scores"
    ]
    
    for query in current_queries:
        print(f"\n   Searching for: '{query}'")
        try:
            result = google_search(query)
            print("   ✅ Search completed!")
            # Show first 200 characters of result
            print("   Sample result:", result[:200] + ("..." if len(result) > 200 else ""))
        except Exception as e:
            print(f"   ❌ Search failed: {e}")
    
    print("\n" + "=" * 50)
    print("Year search testing completed!")

if __name__ == "__main__":
    main()
