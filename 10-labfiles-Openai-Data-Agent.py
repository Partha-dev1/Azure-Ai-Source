#Enviroment
AZURE_OAI_ENDPOINT=https://your-resource-name.openai.azure.com
AZURE_OAI_KEY=your-openai-key
AZURE_OAI_DEPLOYMENT=your-deployment-name
AZURE_SEARCH_ENDPOINT=https://your-search-service-name.search.windows.net
AZURE_SEARCH_KEY=your-search-key
AZURE_SEARCH_INDEX=your-search-index
#Use your own data
import os
import json
from dotenv import load_dotenv
from openai import AzureOpenAI

def main():
    try:
        # Flag to show citations
        show_citations = False

        # Load environment variables
        load_dotenv()
        azure_oai_endpoint = os.getenv("AZURE_OAI_ENDPOINT")
        azure_oai_key = os.getenv("AZURE_OAI_KEY")
        azure_oai_deployment = os.getenv("AZURE_OAI_DEPLOYMENT")
        azure_search_endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")
        azure_search_key = os.getenv("AZURE_SEARCH_KEY")
        azure_search_index = os.getenv("AZURE_SEARCH_INDEX")

        # Initialize the Azure OpenAI client
        client = AzureOpenAI(
            base_url=f"{azure_oai_endpoint}/openai/deployments/{azure_oai_deployment}/extensions",
            api_key=azure_oai_key,
            api_version="2023-09-01-preview"
        )

        # Get the prompt
        text = input('\nEnter a question:\n')

        # Configure your data source
        extension_config = {
            "dataSources": [
                {
                    "type": "AzureCognitiveSearch",
                    "parameters": {
                        "endpoint": azure_search_endpoint,
                        "key": azure_search_key,
                        "indexName": azure_search_index,
                    }
                }
            ]
        }

        # Send request to Azure OpenAI model
        print("...Sending the following request to Azure OpenAI endpoint...")
        print("Request: " + text + "\n")
        
        response = client.chat.completions.create(
            model=azure_oai_deployment,
            temperature=0.5,
            max_tokens=1000,
            messages=[
                {"role": "system", "content": "You are a helpful travel agent"},
                {"role": "user", "content": text}
            ],
            extra_body=extension_config
        )

        # Print response
        print("Response: " + response.choices[0].message.content + "\n")

        if show_citations:
            # Print citations
            print("Citations:")
            citations = response.choices[0].message.context["messages"][0]["content"]
            citation_json = json.loads(citations)
            for c in citation_json["citations"]:
                print(f"  Title: {c['title']}\n    URL: {c['url']}")

    except Exception as ex:
        print("An error occurred:", ex)

if __name__ == '__main__':
    main()
