import os
from dotenv import load_dotenv

print("Current working directory:", os.getcwd())
print("Environment variables before loading .env:")
print("GOOGLE_SEARCH_API_KEY:", os.getenv("GOOGLE_SEARCH_API_KEY"))
print("SEARCH_ENGINE_ID:", os.getenv("SEARCH_ENGINE_ID"))

# Load your API keys from .env
load_dotenv()

print("\nEnvironment variables after loading .env:")
print("GOOGLE_SEARCH_API_KEY:", os.getenv("GOOGLE_SEARCH_API_KEY"))
print("SEARCH_ENGINE_ID:", os.getenv("SEARCH_ENGINE_ID"))

if os.getenv("GOOGLE_SEARCH_API_KEY") and os.getenv("SEARCH_ENGINE_ID"):
    print("\nAPI keys loaded successfully!")
else:
    print("\nWarning: API keys not found or not set properly!")
