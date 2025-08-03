import sys
print("Python version:", sys.version)
print("Python path:", sys.path)

try:
    import os
    print("SUCCESS: os imported")
except Exception as e:
    print("ERROR importing os:", str(e))

try:
    import requests
    print("SUCCESS: requests imported")
except Exception as e:
    print("ERROR importing requests:", str(e))

try:
    from dotenv import load_dotenv
    print("SUCCESS: dotenv imported")
except Exception as e:
    print("ERROR importing dotenv:", str(e))

try:
    from googleapiclient.discovery import build
    print("SUCCESS: googleapiclient imported")
except Exception as e:
    print("ERROR importing googleapiclient:", str(e))

try:
    from duckduckgo_search import DDGS
    print("SUCCESS: duckduckgo_search imported")
except Exception as e:
    print("ERROR importing duckduckgo_search:", str(e))

print("All imports tested!")
