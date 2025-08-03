import os
from dotenv import load_dotenv
from jarvis_search_fixed import google_search

def main():
    # Load environment variables
    load_dotenv()
    
    # Test the google_search function
    print("Testing Google Search function...")
    try:
        result = google_search("Python programming")
        print("✅ Google Search function working correctly!")
        print("Sample result:")
        print(result[:200] + "..." if len(result) > 200 else result)
        return True
    except Exception as e:
        print(f"❌ Google Search function failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    main()
