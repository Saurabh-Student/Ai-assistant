print("Testing minimal import...")
try:
    from dotenv import load_dotenv
    print("✅ python-dotenv: OK")
except ImportError as e:
    print(f"❌ python-dotenv: {e}")

try:
    import livekit.agents
    print("✅ livekit-agents: OK")
except ImportError as e:
    print(f"❌ livekit-agents: {e}")

try:
    import livekit.plugins.google
    print("✅ livekit-plugins-google: OK")
except ImportError as e:
    print(f"❌ livekit-plugins-google: {e}")

try:
    import livekit.plugins.openai
    print("✅ livekit-plugins-openai: OK")
except ImportError as e:
    print(f"❌ livekit-plugins-openai: {e}")

try:
    import livekit.plugins.silero
    print("✅ livekit-plugins-silero: OK")
except ImportError as e:
    print(f"❌ livekit-plugins-silero: {e}")

try:
    import livekit.plugins.noise_cancellation
    print("✅ livekit-plugins-noise-cancellation: OK")
except ImportError as e:
    print(f"❌ livekit-plugins-noise-cancellation: {e}")

try:
    from livekit.agents import tokenize
    print("✅ livekit-agents.tokenize: OK")
except ImportError as e:
    print(f"❌ livekit-agents.tokenize: {e}")

try:
    from livekit.agents.tokenize import blingfire
    print("✅ livekit-agents.tokenize.blingfire: OK")
except ImportError as e:
    print(f"❌ livekit-agents.tokenize.blingfire: {e}")

print("Test completed.")
