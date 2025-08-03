import sys
import traceback

print("Testing APIConnectionError import...")

# Test 1: Check if APIConnectionError exists in livekit.agents
try:
    print("1. Testing direct import of APIConnectionError...")
    from livekit.agents import APIConnectionError
    print("   SUCCESS: APIConnectionError imported directly")
except ImportError as e:
    print(f"   FAILED: {e}")
    
# Test 2: Check what's available in livekit.agents
try:
    print("2. Checking contents of livekit.agents...")
    import livekit.agents
    print("   Available attributes in livekit.agents:")
    for attr in dir(livekit.agents):
        if not attr.startswith('_'):
            print(f"     {attr}")
except Exception as e:
    print(f"   FAILED: {e}")
    traceback.print_exc()

# Test 3: Check if APIConnectionError exists in livekit.agents.llm
try:
    print("3. Testing import from livekit.agents.llm...")
    from livekit.agents.llm import APIConnectionError
    print("   SUCCESS: APIConnectionError imported from llm")
except ImportError as e:
    print(f"   FAILED: {e}")

# Test 4: Check if APIConnectionError exists in livekit.plugins
try:
    print("4. Testing import from livekit.plugins...")
    from livekit.plugins import APIConnectionError
    print("   SUCCESS: APIConnectionError imported from plugins")
except ImportError as e:
    print(f"   FAILED: {e}")

print("\nTest completed.")
