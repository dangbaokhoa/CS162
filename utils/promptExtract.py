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

    response = client.chat.completions.create(
        model = GPT_MODEL,
        messages = [{"role": "user", "content": prompt}],
    )
    response_message = response.choices[0].message
    
    if not response_message or not response_message.content:
        return None, None
    
    extractInfo = json.loads(response_message.content)
    # print(extractInfo)
    if not extractInfo:
        return None, None
    
    for key, value in extractInfo.items():
        if (value): return key, value