import os
import sys

# Add current directory to path
sys.path.insert(0, '.')

# Set environment variables directly
os.environ['GOOGLE_SEARCH_API_KEY'] = 'AIzaSyB0b36lqutN3K7DHuPAuBPOnAhFYpfn8RU'
os.environ['SEARCH_ENGINE_ID'] = 'f469efe96a9aa4e2f'

print("Testing Google Search Integration...")
print("=" * 40)

# Test 1: Import the search function
print("\nTest 1: Importing google_search function...")
try:
    from jarvis_search import google_search
    print("✓ SUCCESS: google_search imported")
except Exception as e:
    print(f"✗ FAILED: {e}")
    sys.exit(1)

# Test 2: Simple search
print("\nTest 2: Performing a simple search...")
try:
    result = google_search("Python programming")
    print("✓ SUCCESS: Search executed")
    print(f"Result length: {len(result)} characters")
    if len(result) > 200:
        print(f"Result preview: {result[:200]}...")
    else:
        print(f"Full result: {result}")
except Exception as e:
    print(f"✗ FAILED: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\n" + "=" * 40)
print("All tests completed successfully!")
print("Google Search integration is working correctly.")
