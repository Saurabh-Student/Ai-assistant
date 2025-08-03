import sys
print(f"Python version: {sys.version}")

try:
    from dotenv import load_dotenv
    print("✅ python-dotenv imported successfully")
except ImportError as e:
    print(f"❌ Failed to import python-dotenv: {e}")

try:
    from livekit import agents
    print("✅ livekit.agents imported successfully")
except ImportError as e:
    print(f"❌ Failed to import livekit.agents: {e}")

try:
    from livekit.agents import AgentSession, Agent, RoomInputOptions
    print("✅ livekit.agents components imported successfully")
except ImportError as e:
    print(f"❌ Failed to import livekit.agents components: {e}")

try:
    from livekit.plugins import google, noise_cancellation
    print("✅ livekit.plugins imported successfully")
except ImportError as e:
    print(f"❌ Failed to import livekit.plugins: {e}")

print("Verification completed.")
