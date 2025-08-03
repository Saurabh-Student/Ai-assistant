import webbrowser
import time

def main():
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
    print("4. Run 'python comprehensive_test.py' to verify")
    print()
    
    # Ask user if they want to open the URL
    response = input("Do you want to open the URL in your browser now? (y/n): ")
    
    if response.lower() in ['y', 'yes']:
        print(f"Opening {url}...")
        webbrowser.open(url)
        print()
        print("💡 After enabling the API:")
        print("   1. Wait 2-5 minutes for propagation")
        print("   2. Run 'python comprehensive_test.py' to verify")
        print("   3. If successful, run 'python agent.py' to start Jarvis")
    else:
        print("You can manually visit this URL later to enable the API:")
        print(url)

if __name__ == "__main__":
    main()
