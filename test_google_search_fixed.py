import os
from dotenv import load_dotenv

# Add current directory to Python path
import sys
sys.path.insert(0, '.')

# Load environment variables
load_dotenv()

def main():
    # Test the google_search function
    print("Testing Google Search function...")
    try:
        from jarvis_search_fixed import google_search
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
