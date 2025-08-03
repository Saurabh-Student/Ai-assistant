import webbrowser
import os
from dotenv import load_dotenv

def main():
    # Load environment variables
    load_dotenv()
    
    # Get the project ID from the error message
    project_id = "703401253493"
    
    # Construct the URL to enable the API
    api_url = f"https://console.developers.google.com/apis/api/customsearch.googleapis.com/overview?project={project_id}"
    
    print("🔧 Google Custom Search API Setup")
    print("=" * 40)
    print(f"Project ID: {project_id}")
    print()
    print("To enable the Google Custom Search API:")
    print("1. The following URL will open in your browser:")
    print(f"   {api_url}")
    print("2. Click on the 'Enable' button")
    print("3. Wait a few minutes for the changes to propagate")
    print("4. Run 'python final_test.py' to verify the integration")
    print()
    
    # Ask user if they want to open the URL
    response = input("Do you want to open the URL in your browser now? (y/n): ")
    
    if response.lower() in ['y', 'yes']:
        print(f"Opening {api_url}...")
        webbrowser.open(api_url)
        print("Please follow the instructions in your browser to enable the API.")
    else:
        print("You can manually visit the URL later to enable the API.")

if __name__ == "__main__":
    main()
