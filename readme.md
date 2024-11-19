AZURE-AI-SOURCE

LAB-01

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

LAB-02

#IMAGE-ANALYSIS
This code demonstrates how to use the Azure AI Vision API to analyze images and remove backgrounds. The code performs image analysis to detect captions, tags, objects, and people, and then removes the background from the image using Azure’s computer vision capabilities.

Features:Image Analysis: Analyzes an image to detect captions, dense captions, tags, objects, and people.

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

git clone <repository_url>
cd <repository_folder>

Install Required Packages:

pip install -r requirements.txt

Set Up Environment Variables:

Create a .env file in the root directory of the project.
Add your Azure AI Vision API Key and Endpoint URL:

AI_SERVICE_ENDPOINT="https://<your-endpoint>.cognitiveservices.azure.com/"
AI_SERVICE_KEY="<your-api-key>"

Add an Image:

Place the image you want to analyze in an images directory at the root of the project.
The default image filename is street.jpg. You can change it by passing the filename as an argument when running the script.
Usage

Run the Main Script:

Run the script to analyze the image and remove the background:

python main.py

Alternatively, specify a custom image file:

python main.py images/your_image.jpg

Output:

The analysis results are printed to the console.
Annotated images with detected objects and people are saved as objects.jpg and people.jpg.
The background-removed image is saved as background.png.

Functions:

main(): Main function to execute the image analysis and background removal processes.

AnalyzeImage(): Analyzes the image for captions, tags, objects, and people.

BackgroundForeground(): Removes the background from the image or generates a foreground matte.

LAB-03

#READ-TEXT
This code leverages Azure's AI Vision services to analyze images and extract text. The script can read and display both printed and handwritten text from provided image files. It uses the Azure AI Vision Read API to detect text, identify bounding polygons, and display results.

Requirements
Python 3.8+
Azure AI Vision SDK: Install via pip:

pip install azure-ai-vision
Environment Variables: Store API credentials securely with .env using python-dotenv:

pip install python-dotenv
Project Structure

main(): Prompts the user to select an image file to analyze.

GetTextRead(image_file): Extracts text from the image, displays bounding polygons, and overlays detected text on the image.
Image Files
Place images you want to analyze in an images folder in the project directory.

Configuration
Create a .env file in the root directory with the following keys:

AI_SERVICE_ENDPOINT="https://<your_service>.cognitiveservices.azure.com/"

AI_SERVICE_KEY="<your_key>"

Ensure your Azure AI Vision resource is set up with READ permissions for text extraction.
Running the Code

Execute the script with:

python <script_name>.py

Select the operation:
Enter 1 to read printed text from Lincoln.jpg.

Enter 2 to read handwritten text from Note.jpg.

The results display extracted text, bounding polygons, and overlays on the image.

Output
Console: Displays detected text with bounding polygons and confidence levels.
Image Output: Saves the image with annotated text as text.jpg in the project directory.

Dependencies

azure-ai-vision
python-dotenv
Pillow
matplotlib

Install dependencies via:

pip install -r requirements.txt

LAB-04

#Text-OpenAI
This project is a Python-based chatbot that uses Azure OpenAI's language capabilities to assist users with hiking suggestions. The bot, named "Forest," provides users with hiking recommendations around Rainier National Park by default but can also make suggestions for other areas if specified by the user. Each recommendation includes a unique insight into the local nature on the hike, enhancing the user experience.

Features
Interactive Chat Interface: Users can ask the chatbot for hiking recommendations.
Dynamic Responses: The chatbot responds with a summary of suggested hikes, each varying in length and including a nature fact.
Customizable Hiking Locations: Users can specify their area of interest, and "Forest" will provide hikes in that region.
User-Friendly Input/Output: Type quit to exit the program or enter prompts to get personalized responses.
Prerequisites
Ensure you have the following:

Python 3.x installed on your machine.

Azure OpenAI account with API keys and endpoints.

Python packages: openai, dotenv. You can install them by running:


pip install openai python-dotenv
Setup
Clone the Repository: Clone this repository to your local machine.


git clone https://github.com/Partha-dev1/azure-openai-hiking-assistant.git
cd azure-openai-hiking-assistant
Environment Variables: Create a .env file in the root directory and add your Azure OpenAI credentials:

AZURE_OAI_ENDPOINT=your_endpoint_here
AZURE_OAI_KEY=your_key_here
AZURE_OAI_DEPLOYMENT=your_deployment_name_here
Run the Script: Start the chatbot by running:


python hiking_assistant.py
Usage
Input Prompts: Enter your hiking queries when prompted. Forest will default to Rainier National Park if no location is provided.
End the Chat: Type quit to exit the program.

LAB-5

#Text Analysis 
This project demonstrates how to leverage Azure AI's Text Analytics service to process text data, analyze sentiment, extract key phrases, and recognize entities from text files.

Features
Detect the language of a text document.
Analyze sentiment (positive, neutral, or negative) of the text.
Extract key phrases to identify significant terms.
Recognize named entities and their categories (e.g., Person, Organization, Location).
Recognize linked entities with associated URLs.
Requirements
Prerequisites
Python 3.8 or later.
Azure subscription with Text Analytics resource created.

.env file containing the following environment variables:
AI_SERVICE_ENDPOINT="Your_Text_Analytics_Endpoint"
AI_SERVICE_KEY="Your_Text_Analytics_Key"

Install required Python packages:

pip install azure-ai-textanalytics python-dotenv

Folder Structure

|-- reviews/          # Folder containing text files to be analyzed.
|-- main.py           # Python script for text analysis.
|-- .env              # Environment file with service credentials.
|-- README.md         # Project documentation.

How to Run
Set Up Environment Variables:
Create a .env file in the project directory and add your Azure Text Analytics endpoint and key.

Prepare Text Files:
Place the text files you want to analyze in the reviews folder.

Run the Script:
Execute the script:

python main.py
View Results:
The script will process each text file in the reviews folder and display the following for each file:

Language
Sentiment
Key phrases
Entities and their categories
Linked entities and URLs

LAB-6

#Question-Answering-Solution
This project provides a simple interface to interact with Azure AI's Language Service for creating a Question Answering (QA) solution. It enables users to ask questions about a specific knowledge base, and the application responds with relevant answers based on the data in the deployed project.

Prerequisites
Before running this application, ensure you have the following:

Azure Account: A valid Azure subscription is required.
Azure Language Service Resource:
A deployed knowledge base (FAQ) in the Question Answering feature of Azure Language Service.
Access to the endpoint URL and API key of the resource.
Python Environment:
Python 3.7 or higher installed.
Dependencies listed in requirements.txt installed.
Installation
Clone this repository or copy the code files into your project directory.

git clone https://github.com/your-repository/question-answering-solution.git
cd question-answering-solution
Create and activate a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the required Python packages:

pip install -r requirements.txt
Configuration
Create an .env file in the root directory of your project and add the following keys:

AI_SERVICE_ENDPOINT="https://<your-service-name>.cognitiveservices.azure.com/"
AI_SERVICE_KEY="<your-api-key>"
QA_PROJECT_NAME="<your-project-name>"
QA_DEPLOYMENT_NAME="<your-deployment-name>"
Replace <your-service-name>, <your-api-key>, <your-project-name>, and <your-deployment-name> with your Azure Language Service credentials.

Running the Application
Run the Python script:

python app.py
Enter a question when prompted. For example:


Question:
What is the refund policy?

Answer:
Refunds are available within 30 days of purchase.
Confidence: 0.95
Source: policy_document.txt
To exit the application, type quit.

Key Features
Interactive interface for submitting questions.
Retrieves answers with confidence scores and sources.
Easy integration with Azure Language Service's Question Answering feature.
Error Handling
If any error occurs, it will be printed to the console. Common issues include:

Incorrect configuration in the .env file.
Network issues connecting to the Azure service.
API quota or authentication failures.
Dependencies

Ensure the following packages are installed:

python-dotenv
azure-core
azure-ai-language-questionanswering

Dependencies are automatically handled when you run:

pip install -r requirements.txt

LAB-7

#
