import os
import sys
from dotenv import load_dotenv

def check_env_vars():
    """Check if all required environment variables are set"""
    print("🔍 Checking environment variables...")
    load_dotenv()
    
    required_vars = [
        "LIVEKIT_API_SECRET",
        "LIVEKIT_URL",
        "GOOGLE_SEARCH_API_KEY",
        "SEARCH_ENGINE_ID"
    ]
    
    all_good = True
    for var in required_vars:
        value = os.getenv(var)
        if not value:
            print(f"  ❌ {var}: Missing")
            all_good = False
        else:
            # Show first and last 5 characters for sensitive data
            if "KEY" in var or "SECRET" in var:
                print(f"  ✅ {var}: {value[:5]}...{value[-5:]}")
            else:
                print(f"  ✅ {var}: {value}")
    
    return all_good

def check_dependencies():
    """Check if all required dependencies are installed"""
    print("\n📦 Checking dependencies...")
    
    required_imports = [
        ("dotenv", "dotenv"),
        ("livekit.agents", "livekit-agents"),
        ("googleapiclient.discovery", "google-api-python-client"),
        ("jarvis_search", "jarvis_search"),
        ("jarvis_prompt", "jarvis_prompt")
    ]
    
    all_good = True
    for module, package in required_imports:
        try:
            __import__(module)
            print(f"  ✅ {package}: Installed")
        except ImportError as e:
            print(f"  ❌ {package}: Missing ({e})")
            all_good = False
    
    return all_good

def check_google_api():
    """Check if Google API is properly configured"""
    print("\n🔍 Checking Google API configuration...")
    
    try:
        from googleapiclient.discovery import build
        from jarvis_search import google_search
        print("  ✅ Google API client: Import successful")
        
        # Check if API key is set
        api_key = os.getenv("GOOGLE_SEARCH_API_KEY")
        if not api_key:
            print("  ❌ Google API key: Not set")
            return False
            
        # Try to build the service
        service = build("customsearch", "v1", developerKey=api_key)
        print("  ✅ Google Custom Search service: Build successful")
        return True
    except Exception as e:
        print(f"  ❌ Google API configuration: Failed ({e})")
        return False

def check_prompt_templates():
    """Check if prompt templates are accessible"""
    print("\n📝 Checking prompt templates...")
    
    try:
        from jarvis_prompt import JarvisPrompt
        print("  ✅ jarvis_prompt module: Import successful")
        
        # Test creating an instance
        prompt = JarvisPrompt()
        print("  ✅ JarvisPrompt class: Instantiation successful")
        
        # Test if templates exist
        if hasattr(prompt, 'system_prompt') and hasattr(prompt, 'user_prompt'):
            print("  ✅ Prompt templates: Accessible")
            return True
        else:
            print("  ❌ Prompt templates: Not found")
            return False
    except Exception as e:
        print(f"  ❌ Prompt templates: Failed ({e})")
        return False

def main():
    """Main verification function"""
    print("🤖 Jarvis Assistant - Final Verification")
    print("=" * 45)
    
    checks = [
        ("Environment Variables", check_env_vars),
        ("Dependencies", check_dependencies),
        ("Google API", check_google_api),
        ("Prompt Templates", check_prompt_templates)
    ]
    
    results = []
    for name, check in checks:
        print(f"\n{name}")
        print("-" * len(name))
        results.append(check())
    
    print("\n📊 Summary")
    print("=" * 45)
    
    passed = sum(results)
    total = len(results)
    
    print(f"Passed: {passed}/{total} checks")
    
    if passed == total:
        print("🎉 All checks passed! Your Jarvis assistant is ready to use.")
        print("\nTo start the assistant, run:")
        print("  python agent.py")
        return True
    else:
        print("⚠️  Some checks failed. Please review the issues above.")
        print("\nFor detailed instructions, check:")
        print("  - ENABLE_API_INSTRUCTIONS.md (for Google API setup)")
        print("  - JARVIS_SETUP_COMPLETE.md (for overall setup completion)")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
