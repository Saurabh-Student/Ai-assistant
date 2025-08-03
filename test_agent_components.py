import sys
import traceback

print("Python version:", sys.version)
print("Testing individual components...\n")

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

# Test 3: jarvis modules
try:
    print("\nTest 3: Importing jarvis modules...")
    from jarvis_prompt import _Behavoiur_prompts, Reply_prompts
    from jarvis_search import google_search
    print("SUCCESS: jarvis modules imported successfully")
except ImportError as e:
    print("FAILED: Could not import jarvis modules")
    print("Error:", str(e))
    traceback.print_exc()

print("\nAll tests completed.")
