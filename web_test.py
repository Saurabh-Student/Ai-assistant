from flask import Flask, request, jsonify
from jarvis_search import google_search
import os

# Set environment variables directly
os.environ['GOOGLE_SEARCH_API_KEY'] = 'AIzaSyB0b36lqutN3K7DHuPAuBPOnAhFYpfn8RU'
os.environ['SEARCH_ENGINE_ID'] = 'f469efe96a9aa4e2f'

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Jarvis Search Test</title>
    </head>
    <body>
        <h1>Jarvis Google Search Test</h1>
        <form action="/search" method="get">
            <input type="text" name="query" placeholder="Enter search query" required>
            <button type="submit">Search</button>
        </form>
    </body>
    </html>
    '''

@app.route('/search')
def search():
    query = request.args.get('query', '')
    if not query:
        return jsonify({'error': 'No query provided'})
    
    try:
        result = google_search(query)
        return f'<h1>Search Results for: {query}</h1><pre>{result}</pre><a href="/">Back to search</a>'
    except Exception as e:
        return f'<h1>Error</h1><p>{str(e)}</p><a href="/">Back to search</a>'

if __name__ == '__main__':
    print("Starting Jarvis Search Test Server...")
    print("Visit http://localhost:5000 to test the search functionality")
    app.run(debug=True, port=5000)
