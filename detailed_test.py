import sys
import traceback
import importlib

print("Python version:", sys.version)
print("Python executable:", sys.executable)

# Try to import livekit module step by step
modules_to_try = [
    "livekit",
    "livekit.agents",
    "livekit.agents.tokenize",
    "livekit.agents.tokenize.blingfire"
]

for module_name in modules_to_try:
    try:
        print(f"\nAttempting to import {module_name}...")
        module = importlib.import_module(module_name)
        print(f"SUCCESS: {module_name} imported successfully")
        if hasattr(module, '__file__'):
            print(f"  Module file: {module.__file__}")
        if hasattr(module, '__path__'):
            print(f"  Module path: {module.__path__}")
    except ImportError as e:
        print(f"FAILED: Could not import {module_name}")
        print(f"  Error: {str(e)}")
        # Print detailed traceback
        traceback.print_exc()
    except Exception as e:
        print(f"UNEXPECTED ERROR: {module_name}")
        print(f"  Error: {str(e)}")
        traceback.print_exc()

print("\nTest completed.")
