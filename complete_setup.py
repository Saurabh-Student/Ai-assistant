import webbrowser
import time
import os
from dotenv import load_dotenv

def main():
    print("🔧 Jarvis AI Assistant - Complete Setup")
    print("=" * 50)
    print()
    
    # Load environment variables
    load_dotenv()
    
    # Check if API key is set
    api_key = os.getenv("GOOGLE_SEARCH_API_KEY")
    if not api_key:
        print("❌ Google Search API key not found in .env file")
        print("Please ensure your .env file contains GOOGLE_SEARCH_API_KEY")
        return
    
    # Get the project ID from the error message
    project_id = "703401253493"
    
    # Construct the URL to enable the API
    api_url = f"https://console.developers.google.com/apis/api/customsearch.googleapis.com/overview?project={project_id}"
    
    print("To enable the Google Custom Search API:")
    print("1. The following URL will open in your browser:")
    print(f"   {api_url}")
    print("2. Click on the 'Enable' button")
    print("3. Wait for the confirmation message that the API is enabled")
    print()
    
    # Ask user if they want to open the URL
    response = input("Do you want to open the URL in your browser now? (y/n): ")
    
    if response.lower() in ['y', 'yes']:
        print(f"Opening {api_url}...")
        webbrowser.open(api_url)
        print()
        print("💡 After enabling the API:")
        print("   1. Wait 1-2 minutes for the changes to propagate")
        print("   2. Run 'python final_test.py' to verify the integration")
        print("   3. If successful, run 'python agent.py' to start Jarvis")
        print()
        print("📌 IMPORTANT: Keep this terminal open and follow the steps in your browser")
    else:
        print("You can manually visit the URL later to enable the API.")
        print("URL:", api_url)
    
    print()
    print("For more detailed instructions, check GOOGLE_API_SETUP.md")

if __name__ == "__main__":
    main()
