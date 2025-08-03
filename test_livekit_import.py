try:
    from livekit import agents
    print("LiveKit agents imported successfully")
except ImportError as e:
    print(f"Import error: {e}")

try:
    from livekit.agents import tokenize
    print("LiveKit tokenize imported successfully")
except ImportError as e:
    print(f"Import error: {e}")

try:
    from livekit.agents.tokenize import blingfire
    print("LiveKit blingfire imported successfully")
except ImportError as e:
    print(f"Import error: {e}")

try:
    import blingfire
    print("Blingfire imported successfully")
except ImportError as e:
    print(f"Blingfire import error: {e}")
