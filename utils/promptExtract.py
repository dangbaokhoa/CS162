import json
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

GPT_MODEL = "gpt-3.5-turbo-0613"
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)
def promptExtract(userPrompt, promptProperty):
    keywords = (', ').join(promptProperty)
    prompt = f"""Extract the following information if it containt similar given keywords and each keyword have, else don't included it and return it as a JSON object with key is: {keywords}.
    This is the body of text to extract the information from:{userPrompt}
    """
    function_descriptions = []
    for key in promptProperty:
        name = f"searchBy{key}"
        description = "Search for the " + key + " in the user prompt"
        parameters = {
            "type": "object",
            "properties": {
                key: {
                    "type": "string",
                    "description": "The " + key + " to search for",
                },
            },
            "required": [key],
        }
        function_descriptions.append({
            "name": name,
            "description": description,
            "parameters": parameters,
        })
    
    response = client.chat.completions.create(
        model = GPT_MODEL,
        messages = [{"role": "user", "content": prompt}],
        functions = function_descriptions,
        function_call="auto"
    )
    response_message = response.choices[0].message
    # print(response_message)
    if not response_message or not response_message.function_call:
        return None
    
    extractInfo = response_message.function_call
    argument = json.loads(extractInfo.arguments)
    chosenFunction = extractInfo.name
    if argument is not None:
        for key, value in argument.items():
            return key, value, chosenFunction
    return None
        