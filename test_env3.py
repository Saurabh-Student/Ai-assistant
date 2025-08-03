import sys
import traceback
import os

print("Python version:", sys.version)
print("Current working directory:", os.getcwd())
print("\nTesting basic imports for Jarvis in env3...\n")

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
    import livekit
    print("SUCCESS: livekit imported successfully")
    print("Livekit version:", getattr(livekit, '__version__', 'Unknown'))
except ImportError as e:
    print("FAILED: Could not import livekit")
    print("Error:", str(e))
    traceback.print_exc()

# Test 3: livekit.agents
try:
    print("\nTest 3: Importing livekit.agents...")
    from livekit import agents
    print("SUCCESS: livekit.agents imported successfully")
except ImportError as e:
    print("FAILED: Could not import livekit.agents")
    print("Error:", str(e))
    traceback.print_exc()

# Test 4: livekit.agents.tokenize
try:
    print("\nTest 4: Importing livekit.agents.tokenize...")
    from livekit.agents import tokenize
    print("SUCCESS: livekit.agents.tokenize imported successfully")
except ImportError as e:
    print("FAILED: Could not import livekit.agents.tokenize")
    print("Error:", str(e))
    traceback.print_exc()

# Test 5: livekit.agents.tokenize.blingfire
try:
    print("\nTest 5: Importing livekit.agents.tokenize.blingfire...")
    from livekit.agents.tokenize import blingfire
    print("SUCCESS: livekit.agents.tokenize.blingfire imported successfully")
except ImportError as e:
    print("FAILED: Could not import livekit.agents.tokenize.blingfire")
    print("Error:", str(e))
    traceback.print_exc()

print("\nAll tests completed.")
