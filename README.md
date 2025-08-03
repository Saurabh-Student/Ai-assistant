# Jarvis AI Assistant

An intelligent AI assistant with Google Search integration, built using LiveKit Agents framework.

## Features
- Voice interaction capabilities
- Google Search integration
- Customizable prompt templates
- LiveKit integration for real-time communication

## Prerequisites
- Python 3.8 or higher
- Google Cloud account with Custom Search API enabled
- LiveKit account

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables
Create a `.env` file with your API keys:
```env
LIVEKIT_API_SECRET=your_livekit_api_secret
LIVEKIT_URL=your_livekit_url
GOOGLE_SEARCH_API_KEY=your_google_search_api_key
SEARCH_ENGINE_ID=your_search_engine_id
```

### 3. Enable Google Custom Search API
1. Visit the [Google Cloud Console](https://console.developers.google.com/apis/api/customsearch.googleapis.com/overview?project=703401253493)
2. Click "Enable" to activate the Custom Search API
3. Wait a few minutes for the changes to propagate

### 4. Verify Setup
Run the verification script to ensure everything is configured correctly:
```bash
python verify_setup.py
```

## Usage

### Start the Assistant
```bash
python agent.py
```

### Run Tests
To verify all components are working:
```bash
python final_test.py
```

## Project Structure
```
├── agent.py              # Main Jarvis agent implementation
├── jarvis_search.py      # Google Search integration
├── jarvis_prompt.py      # Prompt templates
├── requirements.txt      # Python dependencies
├── .env                 # Environment variables (not included in repo)
├── final_test.py        # Comprehensive test script
├── verify_setup.py      # Setup verification script
├── enable_google_api.py # Helper script to enable Google API
├── GOOGLE_API_SETUP.md  # Google API setup guide
└── SETUP_SUMMARY.md     # Setup summary and troubleshooting
```

## Troubleshooting

### Google Search Not Working
If you see a "403 Forbidden" error:
1. Ensure the Custom Search API is enabled in the Google Cloud Console
2. Verify your API key has the necessary permissions
3. Check that your search engine ID is correct

### Dependency Issues
If you encounter import errors:
1. Run `pip install -r requirements.txt` to install all dependencies
2. Ensure you're using Python 3.8 or higher

### Environment Variables
If environment variables are not loading:
1. Verify the `.env` file exists in the project root
2. Check that variable names match exactly

## Additional Resources
- [LiveKit Documentation](https://docs.livekit.io/)
- [Google Custom Search API Documentation](https://developers.google.com/custom-search/v1/intro)
- [Google Cloud Console](https://console.cloud.google.com/)

## License
This project is licensed under the MIT License - see the LICENSE file for details.
