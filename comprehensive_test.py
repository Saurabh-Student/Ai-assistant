import sys
import traceback
import os

print("Python version:", sys.version)
print("Current working directory:", os.getcwd())
print("\nTesting all components for Jarvis...\n")

# Test 1: dotenv
try:
    print("Test 1: Importing dotenv...")
    from dotenv import load_dotenv
    print("SUCCESS: dotenv imported successfully")
except ImportError as e:
    print("FAILED: Could not import dotenv")
    print("Error:", str(e))
    traceback.print_exc()

# Test 2: livekit modules
try:
    print("\nTest 2: Importing livekit modules...")
    from livekit import agents
    from livekit.agents import AgentSession, Agent, RoomInputOptions
    from livekit.plugins import (
        google,
        noise_cancellation,
    )
    print("SUCCESS: livekit modules imported successfully")
except ImportError as e:
    print("FAILED: Could not import livekit modules")
    print("Error:", str(e))
    traceback.print_exc()

# Test 3: jarvis_prompt
try:
    print("\nTest 3: Importing jarvis_prompt...")
    from jarvis_prompt import _Behavoiur_prompts, Reply_prompts
    print("SUCCESS: jarvis_prompt imported successfully")
except ImportError as e:
    print("FAILED: Could not import jarvis_prompt")
    print("Error:", str(e))
    traceback.print_exc()

# Test 4: jarvis_search
try:
    print("\nTest 4: Importing jarvis_search...")
    from jarvis_search import google_search
    print("SUCCESS: jarvis_search imported successfully")
except ImportError as e:
    print("FAILED: Could not import jarvis_search")
    print("Error:", str(e))
    traceback.print_exc()

# Test 5: Check if required environment variables are set
try:
    print("\nTest 5: Checking environment variables...")
    load_dotenv()
    google_api_key = os.getenv("GOOGLE_SEARCH_API_KEY")
    search_engine_id = os.getenv("SEARCH_ENGINE_ID")
    
    if google_api_key:
        print("SUCCESS: GOOGLE_SEARCH_API_KEY found")
    else:
        print("INFO: GOOGLE_SEARCH_API_KEY not found, using default")
        
    if search_engine_id:
        print("SUCCESS: SEARCH_ENGINE_ID found")
    else:
        print("INFO: SEARCH_ENGINE_ID not found, using default")
        
except Exception as e:
    print("ERROR: Could not check environment variables")
    print("Error:", str(e))

print("\nAll tests completed.")
