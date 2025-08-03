import os
from dotenv import load_dotenv
from jarvis_search import google_search

def main():
    # Load environment variables
    load_dotenv()
    
    print("Testing Jarvis Current Search Functionality")
    print("=" * 50)
    
    # Test cases for current data searches
    test_queries = [
        "current weather in New York",
        "latest news about technology",
        "what time is it in London",
        "current stock price of Apple",
        "latest sports scores"
    ]
    
    for i, query in enumerate(test_queries, 1):
        print(f"\nTest {i}: Searching for '{query}'")
        print("-" * 30)
        
        try:
            result = google_search(query)
            print("Result:")
            print(result)
            print("Status: ✅ Success" if "sorry" not in result.lower() and "error" not in result.lower() else "Status: ❌ Failed")
        except Exception as e:
            print(f"Status: ❌ Failed with exception: {e}")
        
        # Add a separator between tests
        if i < len(test_queries):
            print("\n" + "="*50)
    
    print("\n" + "="*50)
    print("Testing completed!")

if __name__ == "__main__":
    main()
