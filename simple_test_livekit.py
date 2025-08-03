import sys
import traceback

print("Python version:", sys.version)

try:
    print("Attempting to import livekit.agents...")
    from livekit import agents
    print("SUCCESS: livekit.agents imported successfully")
except ImportError as e:
    print("FAILED: Could not import livekit.agents")
    print("Error:", str(e))
    traceback.print_exc()

try:
    print("Attempting to import livekit.agents.tokenize...")
    from livekit.agents import tokenize
    print("SUCCESS: livekit.agents.tokenize imported successfully")
except ImportError as e:
    print("FAILED: Could not import livekit.agents.tokenize")
    print("Error:", str(e))
    traceback.print_exc()

try:
    print("Attempting to import livekit.agents.tokenize.blingfire...")
    from livekit.agents.tokenize import blingfire
    print("SUCCESS: livekit.agents.tokenize.blingfire imported successfully")
except ImportError as e:
    print("FAILED: Could not import livekit.agents.tokenize.blingfire")
    print("Error:", str(e))
    traceback.print_exc()

print("Test completed.")
