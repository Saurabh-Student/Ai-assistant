import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set the API keys from the documentation if not in environment
GOOGLE_SEARCH_API_KEY = os.getenv('GOOGLE_SEARCH_API_KEY') or 'AIzaSyB0b36lqutN3K7DHuPAuBPOnAhFYpfn8RU'
SEARCH_ENGINE_ID = os.getenv('SEARCH_ENGINE_ID') or 'f469efe96a9aa4e2f'

print("Checking environment variables...")
print(f"GOOGLE_SEARCH_API_KEY: {GOOGLE_SEARCH_API_KEY}")
print(f"SEARCH_ENGINE_ID: {SEARCH_ENGINE_ID}")

if GOOGLE_SEARCH_API_KEY:
    print("✅ GOOGLE_SEARCH_API_KEY is set")
else:
    print("❌ GOOGLE_SEARCH_API_KEY is NOT set")

if SEARCH_ENGINE_ID:
    print("✅ SEARCH_ENGINE_ID is set")
else:
    print("❌ SEARCH_ENGINE_ID is NOT set")
