#REST-CLIENT

#SDK-CLIENT
Language Detection with Azure Cognitive Services Text Analytics
This code demonstrates how to use the Azure Cognitive Services Text Analytics API to detect the primary language of a given text string.
Requirements: Python 3.x
azure-ai-textanalytics library (install using pip install azure-ai-textanalytics)
An Azure Cognitive Services Text Analytics resource with an endpoint and key
Getting Started: Create an Azure Cognitive Services Text Analytics Resource: 
Follow the instructions on the Azure portal (https://learn.microsoft.com/en-us/azure/synapse-analytics/machine-learning/tutorial-text-analytics-use-mmlspark) to create a Text Analytics resource.
Obtain your Endpoint and Key: Navigate to your Text Analytics resource in the Azure portal. Under "Essentials," copy the "Endpoint" and "Primary Key" values.
Configuration: Replace YOUR_AI_SERVICES_ENDPOINT and YOUR_AI_SERVICES_KEY in the environment variables section with your actual values obtained from Azure.
Code Breakdown: 
Environment Variables: The code uses the dotenv library to load environment variables from a .env file. This ensures your credentials are not stored directly in the code.
main Function: 
Establishes global variables ai_endpoint and ai_key to store the loaded credentials. Loads environment variables using load_dotenv(). Retrieves the endpoint and key from environment variables. Enters a loop to continuously prompt the user for text input. If the user enters a text string other than "quit", calls the GetLanguage function to detect the language. Prints the detected language. An exception handler catches any errors that may occur during the process.
GetLanguage Function:
Creates an AzureKeyCredential object using the retrieved API key.
Initializes a TextAnalyticsClient instance with the endpoint and credential.
Calls the client.detect_language method to analyze the provided text for its language.
Extracts and returns the primary language name from the detected language object.
Instructions:
Create a .env file:
In the project directory, create a file named .env.
Add the following lines, replacing the placeholders with your actual values:
AI_SERVICE_ENDPOINT=YOUR_AZURE_TEXT_ANALYTICS_ENDPOINT
AI_SERVICE_KEY=YOUR_AZURE_TEXT_ANALYTICS_KEY
Important: Avoid committing the .env file to version control systems like Git.
Run the Script:
Open a terminal or command prompt and navigate to the project directory.
Execute the Python script using python script_name.py (replace script_name.py with the actual filename).
