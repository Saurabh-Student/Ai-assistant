import sys
import traceback
import os

print("Python version:", sys.version)
print("Current working directory:", os.getcwd())
print("\nFinal test for Jarvis components...\n")

# Test 1: All required imports
try:
    print("Test 1: Importing all required modules...")
    from dotenv import load_dotenv
    from livekit import agents
    from livekit.agents import AgentSession, Agent, RoomInputOptions
    from livekit.plugins import (
        google,
        noise_cancellation,
    )
    from jarvis_prompt import _Behavoiur_prompts, Reply_prompts
    from jarvis_search import google_search
    print("SUCCESS: All modules imported successfully")
except ImportError as e:
    print("FAILED: Could not import required modules")
    print("Error:", str(e))
    traceback.print_exc()

# Test 2: Check if tokenize module works
try:
    print("\nTest 2: Testing tokenize module...")
    from livekit.agents.tokenize import blingfire
    print("SUCCESS: tokenize module works correctly")
except ImportError as e:
    print("FAILED: tokenize module not working")
    print("Error:", str(e))
    traceback.print_exc()

# Test 3: Check if agent can be instantiated
try:
    print("\nTest 3: Testing agent instantiation...")
    
    class Assistant(agents.Agent):
        def __init__(self) -> None:
            super().__init__(instructions=_Behavoiur_prompts, tools=[google_search])
    
    assistant = Assistant()
    print("SUCCESS: Agent instantiated correctly")
except Exception as e:
    print("FAILED: Could not instantiate agent")
    print("Error:", str(e))
    traceback.print_exc()

print("\nFinal test completed.")
