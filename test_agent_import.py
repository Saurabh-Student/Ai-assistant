import sys
import traceback

print("Python version:", sys.version)
print("Testing agent.py import...\n")

try:
    print("Attempting to import agent.py...")
    import agent
    print("SUCCESS: agent.py imported successfully")
except ImportError as e:
    print("FAILED: Could not import agent.py")
    print("Error:", str(e))
    traceback.print_exc()
except Exception as e:
    print("FAILED: Unexpected error while importing agent.py")
    print("Error:", str(e))
    traceback.print_exc()

print("\nTest completed.")
