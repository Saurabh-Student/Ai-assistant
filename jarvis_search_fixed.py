import os
import requests
import json
import re
from datetime import datetime
from dotenv import load_dotenv

# Load your API keys from .env
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_SEARCH_API_KEY") or 'AIzaSyB0b36lqutN3K7DHuPAuBPOnAhFYpfn8RU'
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID") or 'f469efe96a9aa4e2f'

def format_current_time():
    """Get current time for context in searches"""
    now = datetime.now()
    return now.strftime("%B %d, %Y at %I:%M %p")

def is_year_search(query: str) -> bool:
    """Detect if the query is specifically searching for a year"""
    # Check if query contains a 4-digit year (like 2025)
    year_pattern = r'\b(19|20)\d{2}\b'
    years = re.findall(year_pattern, query)
    
    # If we find years in the query, check if they're the main focus
    if years:
        # Simple heuristic: if query is short and contains a year, it's likely a year search
        if len(query.split()) <= 4:
            return True
        # Check if query explicitly mentions the year
        for year in years:
            if str(year) in query:
                return True
    return False

def enhanced_duckduckgo_search(query: str) -> str:
    """Performs an enhanced DuckDuckGo search with better handling for current data."""
    try:
        from duckduckgo_search import DDGS
        
        # Check if this is a year-specific search
        if not is_year_search(query):
            # Add current context to query for more relevant results
            current_time = format_current_time()
            enhanced_query = f"{query} current information {current_time}"
        else:
            # For year-specific searches, use the query as-is
            enhanced_query = query
        
        ddgs = DDGS()
        results = ddgs.text(enhanced_query, max_results=5)
        
        if not results:
            # Try original query if enhanced query fails
            results = ddgs.text(query, max_results=5)
            
        if not results:
            return "I'm sorry, no results were found for your query."
        
        # Add context about when the search was performed
        if is_year_search(query):
            output = f"Here's what I found about '{query}':\n\n"
        else:
            current_time = format_current_time()
            output = f"Here's what I found about '{query}' (as of {current_time}):\n\n"
            
        for i, result in enumerate(results[:3], 1):  # Limit to top 3 results
            title = result.get('title', 'No title')
            link = result.get('href', result.get('link', 'No link'))
            snippet = result.get('body', '')[:200] + "..." if len(result.get('body', '')) > 200 else result.get('body', '')
            
            output += f"{i}. *{title}*\n"
            if snippet:
                output += f"   {snippet}\n"
            output += f"   {link}\n\n"
        return output
    except Exception as e:
        return f"I'm having trouble searching for that information right now. Error: {str(e)}"

def enhanced_google_search(query: str) -> str:
    """Performs an enhanced Google search with better error handling."""
    try:
        if not GOOGLE_API_KEY or not SEARCH_ENGINE_ID:
            raise ValueError("Google API key or Search Engine ID not found")
        
        from googleapiclient.discovery import build
        
        # Check if this is a year-specific search
        if not is_year_search(query):
            # Add current context to query
            current_time = format_current_time()
            enhanced_query = f"{query} current information {current_time}"
        else:
            # For year-specific searches, use the query as-is
            enhanced_query = query
        
        service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)
        results = service.cse().list(
            q=enhanced_query, 
            cx=SEARCH_ENGINE_ID, 
            num=3,
            safe="active"  # Enable safe search
        ).execute()
        
        if 'items' not in results:
            # Try original query
            results = service.cse().list(
                q=query, 
                cx=SEARCH_ENGINE_ID, 
                num=3,
                safe="active"
            ).execute()
            
            if 'items' not in results:
                return "I'm sorry, no results were found for your query."
        
        # Add context about when the search was performed
        if is_year_search(query):
            output = f"Here's what I found about '{query}':\n\n"
        else:
            current_time = format_current_time()
            output = f"Here's what I found about '{query}' (as of {current_time}):\n\n"
            
        for i, item in enumerate(results["items"][:3], 1):  # Limit to top 3 results
            title = item.get('title', 'No title')
            link = item.get('link', 'No link')
            snippet = item.get('snippet', '')[:200] + "..." if len(item.get('snippet', '')) > 200 else item.get('snippet', '')
            
            output += f"{i}. *{title}*\n"
            if snippet:
                output += f"   {snippet}\n"
            output += f"   {link}\n\n"
        return output
    except Exception as e:
        return f"Google search is temporarily unavailable. Error: {str(e)}"

def google_search_fallback(query: str) -> str:
    """Performs a Google search using requests as a fallback method."""
    try:
        if not GOOGLE_API_KEY or not SEARCH_ENGINE_ID:
            raise ValueError("Google API key or Search Engine ID not found")
            
        # Check if this is a year-specific search
        if not is_year_search(query):
            # Add current context to query
            current_time = format_current_time()
            enhanced_query = f"{query} current information {current_time}"
        else:
            # For year-specific searches, use the query as-is
            enhanced_query = query
        
        url = f"https://www.googleapis.com/customsearch/v1"
        params = {
            'key': GOOGLE_API_KEY,
            'cx': SEARCH_ENGINE_ID,
            'q': enhanced_query,
            'num': 3,
            'safe': 'active'
        }
        response = requests.get(url, params=params, timeout=10)
        
        if response.status_code != 200:
            # Try original query
            params['q'] = query
            response = requests.get(url, params=params, timeout=10)
            
        response.raise_for_status()
        results = response.json()
        
        if 'items' not in results:
            return "I'm sorry, no results were found for your query."
        
        # Add context about when the search was performed
        if is_year_search(query):
            output = f"Here's what I found about '{query}':\n\n"
        else:
            current_time = format_current_time()
            output = f"Here's what I found about '{query}' (as of {current_time}):\n\n"
            
        for i, item in enumerate(results["items"][:3], 1):  # Limit to top 3 results
            title = item.get('title', 'No title')
            link = item.get('link', 'No link')
            snippet = item.get('snippet', '')[:200] + "..." if len(item.get('snippet', '')) > 200 else item.get('snippet', '')
            
            output += f"{i}. *{title}*\n"
            if snippet:
                output += f"   {snippet}\n"
            output += f"   {link}\n\n"
        return output
    except Exception as e:
        return f"Google search is temporarily unavailable. Error: {str(e)}"

# Define the main Google Search tool without @function_tool decorator
def google_search(query: str) -> str:
    """
    Performs a Google search for information and returns results.
    This function intelligently handles both current information searches and specific year searches.
    For current searches, it adds context about when the search was performed.
    For year-specific searches (like 2025), it searches for that specific year without adding current context.
    """
    
    # Log the search query for debugging
    print(f"Searching for: '{query}'")
    
    # First, try Google Custom Search with enhanced features
    try:
        result = enhanced_google_search(query)
        if "sorry" not in result.lower() and "error" not in result.lower():
            return result
    except Exception as e:
        print(f"Enhanced Google search failed: {e}")
    
    # Try fallback method
    try:
        result = google_search_fallback(query)
        if "sorry" not in result.lower() and "error" not in result.lower():
            return result
    except Exception as e:
        print(f"Google search fallback failed: {e}")
    
    # If Google search fails, try DuckDuckGo as final fallback
    try:
        result = enhanced_duckduckgo_search(query)
        return result
    except Exception as e:
        print(f"DuckDuckGo search failed: {e}")
        return f"I'm unable to search for information right now. Please try again later."
