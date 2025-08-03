import sys
import traceback

print("Testing LiveKit API compatibility...")

# Test imports
try:
    print("1. Testing basic livekit.agents import...")
    import livekit.agents
    print("   SUCCESS: livekit.agents imported")
except Exception as e:
    print(f"   FAILED: {e}")
    traceback.print_exc()

try:
    print("2. Testing specific imports from livekit.agents...")
    from livekit.agents import Agent, JobContext
    print("   SUCCESS: Agent and JobContext imported")
except Exception as e:
    print(f"   FAILED: {e}")
    traceback.print_exc()

try:
    print("3. Testing livekit.plugins imports...")
    from livekit.plugins import google, openai
    print("   SUCCESS: google and openai plugins imported")
except Exception as e:
    print(f"   FAILED: {e}")
    traceback.print_exc()

try:
    print("4. Testing noise cancellation import...")
    from livekit.plugins import noise_cancellation
    print("   SUCCESS: noise_cancellation imported")
except Exception as e:
    print(f"   FAILED: {e}")
    traceback.print_exc()

try:
    print("5. Testing tokenize import...")
    from livekit.agents import tokenize
    print("   SUCCESS: tokenize imported")
except Exception as e:
    print(f"   FAILED: {e}")
    traceback.print_exc()

try:
    print("6. Testing blingfire import...")
    from livekit.agents.tokenize import blingfire
    print("   SUCCESS: blingfire imported")
except Exception as e:
    print(f"   FAILED: {e}")
    traceback.print_exc()

print("\nTest completed.")
