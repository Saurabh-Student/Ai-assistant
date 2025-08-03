import webbrowser
import time
import os
from dotenv import load_dotenv

def enable_api():
    """Help user enable the Google Custom Search API"""
    # URL to enable the Custom Search API
    url = "https://console.developers.google.com/apis/api/customsearch.googleapis.com/overview?project=703401253493"
    
    print("🔧 Google Custom Search API - Enablement Helper")
    print("=" * 50)
    print()
    print("This script will help you enable the Google Custom Search API.")
    print()
    print("Instructions:")
    print("1. The Google Cloud Console page will open in your browser")
    print("2. Click the 'Enable' button to enable the API")
    print("3. Wait 2-5 minutes for the changes to propagate")
    print("4. Run 'python final_verification.py' to verify")
    print()
    
    # Ask user if they want to open the URL
    response = input("Do you want to open the URL in your browser now? (y/n): ")
    
    if response.lower() in ['y', 'yes']:
        print(f"Opening {url}...")
        webbrowser.open(url)
        print()
        print("💡 After enabling the API:")
        print("   1. Wait 2-5 minutes for propagation")
        print("   2. Run 'python final_verification.py' to verify")
        print("   3. If successful, run 'python agent.py' to start Jarvis")
        return True
    else:
        print("You can manually visit this URL later to enable the API:")
        print(url)
        return False

def verify_api():
    """Verify that the Google Custom Search API is enabled and working"""
    print("\n🔍 Verifying Google Custom Search API...")
    
    # Load environment variables
    load_dotenv()
    
    # Check if API key is set
    api_key = os.getenv("GOOGLE_SEARCH_API_KEY")
    if not api_key:
        print("❌ Google Search API key not found in .env file")
        return False
    
    # Check if Search Engine ID is set
    search_engine_id = os.getenv("SEARCH_ENGINE_ID")
    if not search_engine_id:
        print("❌ Search Engine ID not found in .env file")
        return False
    
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
            print("   Please visit the Google Cloud Console and click 'Enable' to activate the API.")
        else:
            print(f"❌ Google Custom Search API: Request failed ({e})")
        return False

def main():
    """Main function"""
    print("🤖 Jarvis AI Assistant - Enable and Verify Google API")
    print()
    
    # Help user enable the API
    api_enabled = enable_api()
    
    if api_enabled:
        print("\n⏳ Please wait 2-5 minutes for the API to be enabled...")
        print("   After waiting, run 'python final_verification.py' to verify")
    else:
        print("\n💡 To verify the API is working:")
        print("   1. Make sure you've enabled the API in the Google Cloud Console")
        print("   2. Wait 2-5 minutes for propagation")
        print("   3. Run 'python final_verification.py'")

if __name__ == "__main__":
    main()
