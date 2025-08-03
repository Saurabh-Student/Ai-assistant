# Google Custom Search API Setup Guide

## Issue
The Jarvis assistant is unable to perform Google searches because the Custom Search API is not enabled in your Google Cloud project.

## Current Configuration
- **Project ID**: 703401253493
- **API Key**: AIzaSyB0b36lqutN3K7DHuPAuBPOnAhFYpfn8RU
- **Search Engine ID**: f469efe96a9aa4e2f

## Solution
You need to enable the Custom Search API in the Google Cloud Console.

## Steps to Enable the API

1. **Visit the Google Cloud Console**
   - Go to: https://console.developers.google.com/apis/api/customsearch.googleapis.com/overview?project=703401253493

2. **Enable the API**
   - Click on the "Enable" button to enable the Custom Search API for your project.

3. **Wait for Propagation**
   - After enabling the API, wait a few minutes for the changes to propagate through Google's systems.

4. **Test the Integration**
   - Run the test script again:
     ```
     python final_test.py
     ```

## Alternative: Create a New Project

If you prefer to use a different project or if there are issues with the current project:

1. **Create a New Project**
   - Go to the Google Cloud Console: https://console.cloud.google.com/
   - Create a new project or select an existing one.

2. **Enable the Custom Search API**
   - Navigate to "APIs & Services" > "Library"
   - Search for "Custom Search API"
   - Click on it and then click "Enable"

3. **Get Your API Key**
   - Go to "APIs & Services" > "Credentials"
   - Create a new API key or use an existing one

4. **Update Your Environment Variables**
   - Update the `.env` file with your new API key:
     ```
     GOOGLE_SEARCH_API_KEY=your_new_api_key_here
     SEARCH_ENGINE_ID=f469efe96a9aa4e2f
     ```

## Verification

After enabling the API, you should see all tests pass when running:
```
python final_test.py
```

The output should show:
```
Final Result: 4/4 tests passed
🎉 All tests passed! The Google Search integration is working correctly.
```

## Additional Notes

- Make sure your API key has the necessary permissions for the Custom Search API
- Ensure that your search engine ID is correctly configured in the Google Custom Search Engine control panel
- If you continue to experience issues, check the Google Cloud Console for any error messages or quota exceeded warnings
