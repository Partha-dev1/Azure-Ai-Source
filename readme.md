AZURE-AI-SOURCE

#REST-CLIENT
Language Detection with Azure Cognitive Services Text Analytics (REST API)
This code demonstrates how to detect the primary language of a given text string using the Azure Cognitive Services Text Analytics API's REST interface.

Requirements:
Python 3.x
Standard libraries: http.client, base64, json, urllib
An Azure Cognitive Services Text Analytics resource with an endpoint and key
Getting Started:

Create an Azure Cognitive Services Text Analytics Resource:
Follow the instructions on the Azure portal (https://learn.microsoft.com/en-us/azure/synapse-analytics/machine-learning/tutorial-text-analytics-use-mmlspark) to create a Text Analytics resource.

Obtain your Endpoint and Key:
Navigate to your Text Analytics resource in the Azure portal.
Under "Essentials," copy the "Endpoint" and "Primary Key" values.

Configuration:
Replace YOUR_AI_SERVICES_ENDPOINT and YOUR_AI_SERVICES_KEY in the environment variables section with your actual values obtained from Azure.
Code Breakdown:
Environment Variables:
The code does not use dotenv in this case, but you can still consider adding it for improved security.

main Function:
Establishes global variables ai_endpoint and ai_key to store the loaded credentials.
Enters a loop to continuously prompt the user for text input.
If the user enters a text string other than "quit", calls the GetLanguage function to detect the language.
An exception handler catches any errors that may occur during the process.

GetLanguage Function:
Constructs a JSON request body with a document containing the user's text.
Prints the formatted JSON body for reference.
Establishes an HTTPS connection to the Text Analytics service endpoint.
Defines headers for content type and authentication using the API key.
Sends a POST request with the JSON body and headers to the /text/analytics/v3.1/languages? endpoint.
Retrieves the response data and checks the status code for success (200).
If successful, parses the JSON response.
Prints the complete response (optional, for debugging).
Iterates through each document in the response and prints the detected language name.
If the request fails, prints the entire error response.
Closes the HTTP connection.

Instructions:
Run the Script:
Open a terminal or command prompt and navigate to the project directory.
Execute the Python script using python script_name.py (replace script_name.py with the actual filename).


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


#IMAGE-ANALYSIS
This code demonstrates how to use the Azure AI Vision API to analyze images and remove backgrounds. The code performs image analysis to detect captions, tags, objects, and people, and then removes the background from the image using Azure’s computer vision capabilities.

Features:

Image Analysis: Analyzes an image to detect captions, dense captions, tags, objects, and people.
Background Removal: Removes the background of an image, saving the processed image locally.
Prerequisites
Python 3.7+
Azure subscription with AI Vision services enabled
Azure AI Vision API Key and Endpoint URL

Required Python packages:

dotenv
Pillow
matplotlib
requests
azure-ai-vision
azure-core
Setup

Clone the Repository:
bash
Copy code
git clone <repository_url>
cd <repository_folder>

Install Required Packages:

bash
Copy code
pip install -r requirements.txt

Set Up Environment Variables:

Create a .env file in the root directory of the project.
Add your Azure AI Vision API Key and Endpoint URL:
plaintext
Copy code
AI_SERVICE_ENDPOINT="https://<your-endpoint>.cognitiveservices.azure.com/"
AI_SERVICE_KEY="<your-api-key>"

Add an Image:

Place the image you want to analyze in an images directory at the root of the project.
The default image filename is street.jpg. You can change it by passing the filename as an argument when running the script.
Usage

Run the Main Script:

Run the script to analyze the image and remove the background:
bash
Copy code
python main.py

Alternatively, specify a custom image file:
bash
Copy code
python main.py images/your_image.jpg

Output:

The analysis results are printed to the console.
Annotated images with detected objects and people are saved as objects.jpg and people.jpg.
The background-removed image is saved as background.png.

Functions:

main(): Main function to execute the image analysis and background removal processes.
AnalyzeImage(): Analyzes the image for captions, tags, objects, and people.
BackgroundForeground(): Removes the background from the image or generates a foreground matte.
