# Enable Google Custom Search API - Step by Step Guide

## Current Issue
The Jarvis AI assistant is unable to perform Google searches because the Custom Search API is not enabled in your Google Cloud project.

## Solution
You need to enable the Custom Search API in the Google Cloud Console.

## Step-by-Step Instructions

### Step 1: Open the Google Cloud Console
1. Click on this link to open the Google Cloud Console:
   https://console.developers.google.com/apis/api/customsearch.googleapis.com/overview?project=703401253493

### Step 2: Enable the API
1. Once the page loads, look for a blue "Enable" button
2. Click the "Enable" button
3. Wait for the confirmation message that the API has been enabled

### Step 3: Wait for Propagation
1. After enabling the API, wait 2-5 minutes for the changes to propagate through Google's systems
2. This is an important step - the API will not work immediately after enabling

### Step 4: Verify the Integration
1. After waiting, run the test script to verify everything is working:
   ```
   python comprehensive_test.py
   ```

## Alternative Method: Manual Navigation

If the direct link doesn't work, you can enable the API manually:

1. Go to the Google Cloud Console: https://console.cloud.google.com/
2. Make sure you're in the correct project (Project ID: 703401253493)
3. Navigate to "APIs & Services" > "Library"
4. Search for "Custom Search API"
5. Click on "Custom Search API" in the search results
6. Click the "Enable" button

## Troubleshooting

### If You Still Get a 403 Error After Enabling the API

1. **Double-check the API is enabled**
   - Visit: https://console.developers.google.com/apis/dashboard?project=703401253493
   - Verify that "Custom Search API" is listed as enabled

2. **Wait a bit longer**
   - Sometimes it takes 5-10 minutes for the API enablement to propagate

3. **Check your API key restrictions**
   - Visit: https://console.cloud.google.com/apis/credentials
   - Make sure your API key doesn't have IP restrictions that might block requests

## Important Notes

- The project ID is: 703401253493
- The API key is in your `.env` file
- The Search Engine ID is: f469efe96a9aa4e2f

## After Enabling the API

Once you've enabled the API and waited for propagation:

1. Run the comprehensive test:
   ```
   python comprehensive_test.py
   ```

2. If all tests pass, start the Jarvis assistant:
   ```
   python agent.py
   ```

## Need More Help?

If you continue to experience issues:

1. Check the Google Cloud Console for any error messages
2. Verify your API key has the necessary permissions
3. Ensure your search engine ID is correctly configured
