import os
import sys
from dotenv import load_dotenv

def test_google_api():
    """Test if Google Custom Search API is enabled and working"""
    print("🔍 Testing Google Custom Search API...")
    
    # Load environment variables
    load_dotenv()
    
    # Check if API key is set
    api_key = os.getenv("GOOGLE_SEARCH_API_KEY")
    if not api_key:
        print("❌ Google Search API key not found in .env file")
        return False
    
    print(f"✅ API Key: {api_key[:10]}...{api_key[-5:]}")
    
    # Check if Search Engine ID is set
    search_engine_id = os.getenv("SEARCH_ENGINE_ID")
    if not search_engine_id:
        print("❌ Search Engine ID not found in .env file")
        return False
    
    print(f"✅ Search Engine ID: {search_engine_id}")
    
    # Try to import Google API client
    try:
        from googleapiclient.discovery import build
        print("✅ Google API Client: Import successful")
    except ImportError as e:
        print(f"❌ Google API Client: Import failed ({e})")
        return False
    
    # Try to build the service
    try:
        service = build("customsearch", "v1", developerKey=api_key)
        print("✅ Google Custom Search Service: Build successful")
    except Exception as e:
        print(f"❌ Google Custom Search Service: Build failed ({e})")
        return False
    
    # Try to make a simple request to check if API is enabled
    try:
        print("🔍 Testing API request...")
        result = service.cse().list(q="test", cx=search_engine_id, num=1).execute()
        print("✅ Google Custom Search API: Request successful")
        print("🎉 The Google Custom Search API is properly configured and enabled!")
        return True
    except Exception as e:
        error_msg = str(e)
        if "accessNotConfigured" in error_msg:
            print("❌ Google Custom Search API: Not enabled")
            print("   The API is not enabled in your Google Cloud project.")
            print("   Please visit: https://console.developers.google.com/apis/api/customsearch.googleapis.com/overview?project=703401253493")
            print("   and click 'Enable' to activate the API.")
        else:
            print(f"❌ Google Custom Search API: Request failed ({e})")
        return False

def main():
    """Main function"""
    print("🤖 Jarvis AI Assistant - Google API Test")
    print()
    
    success = test_google_api()
    
    if success:
        print()
        print("🎉 All systems are go!")
        print("You can now run the Jarvis assistant with:")
        print("  python agent.py")
    else:
        print()
        print("🔧 Troubleshooting steps:")
        print("1. Check your API key in the .env file")
        print("2. Ensure the Google Custom Search API is enabled")
        print("3. Wait a few minutes after enabling the API for changes to propagate")
        print("4. Run this script again to verify")

if __name__ == "__main__":
    main()
