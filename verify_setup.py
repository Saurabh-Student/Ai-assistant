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
    
    missing_vars = []
    for var in required_vars:
        value = os.getenv(var)
        if not value:
            missing_vars.append(var)
            print(f"  ❌ {var}: Missing")
        else:
            # Show first and last 5 characters for sensitive data
            if "KEY" in var or "SECRET" in var:
                print(f"  ✅ {var}: {value[:5]}...{value[-5:]}")
            else:
                print(f"  ✅ {var}: {value}")
    
    if missing_vars:
        print(f"  ⚠️  Missing {len(missing_vars)} environment variables")
        return False
    else:
        print("  🎉 All environment variables are set")
        return True

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
    
    missing_deps = []
    for module, package in required_imports:
        try:
            __import__(module)
            print(f"  ✅ {package}: Installed")
        except ImportError as e:
            missing_deps.append(package)
            print(f"  ❌ {package}: Missing ({e})")
    
    if missing_deps:
        print(f"  ⚠️  Missing {len(missing_deps)} dependencies")
        return False
    else:
        print("  🎉 All dependencies are installed")
        return True

def check_files():
    """Check if all required files exist"""
    print("\n📁 Checking required files...")
    
    required_files = [
        "agent.py",
        "jarvis_search.py",
        "jarvis_prompt.py",
        "requirements.txt",
        ".env"
    ]
    
    missing_files = []
    for file in required_files:
        if os.path.exists(file):
            print(f"  ✅ {file}: Exists")
        else:
            missing_files.append(file)
            print(f"  ❌ {file}: Missing")
    
    if missing_files:
        print(f"  ⚠️  Missing {len(missing_files)} files")
        return False
    else:
        print("  🎉 All required files exist")
        return True

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

def main():
    """Main verification function"""
    print("🤖 Jarvis Assistant Setup Verification")
    print("=" * 40)
    
    checks = [
        check_env_vars,
        check_dependencies,
        check_files,
        check_google_api
    ]
    
    results = []
    for check in checks:
        results.append(check())
    
    print("\n📊 Summary")
    print("=" * 40)
    
    passed = sum(results)
    total = len(results)
    
    print(f"Passed: {passed}/{total} checks")
    
    if passed == total:
        print("🎉 All checks passed! Your Jarvis assistant is ready to use.")
        print("\nTo start the assistant, run:")
        print("  python agent.py")
    else:
        print("⚠️  Some checks failed. Please review the issues above.")
        print("\nFor detailed instructions, check:")
        print("  - GOOGLE_API_SETUP.md (for Google API setup)")
        print("  - SETUP_SUMMARY.md (for overall setup summary)")

if __name__ == "__main__":
    main()
